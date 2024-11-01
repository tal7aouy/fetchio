import requests
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Http:
    _instance = None
    _initialized = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Http, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.logger = logging.getLogger(__name__)
            self.session = requests.Session()
            retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
            self.session.mount('http://', HTTPAdapter(max_retries=retries))
            self.session.mount('https://', HTTPAdapter(max_retries=retries))
            self._initialized = True

    def get(self, url, params=None, headers=None, timeout=10):
        self.logger.debug(f"GET request to {url} with params {params} and headers {headers}")
        response = self.session.get(url, params=params, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def post(self, url, data=None, json=None, headers=None, timeout=10):
        self.logger.debug(f"POST request to {url} with data {data}, json {json}, and headers {headers}")
        response = self.session.post(url, data=data, json=json, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def put(self, url, data=None, json=None, headers=None, timeout=10):
        self.logger.debug(f"PUT request to {url} with data {data}, json {json}, and headers {headers}")
        response = self.session.put(url, data=data, json=json, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def delete(self, url, headers=None, timeout=10):
        self.logger.debug(f"DELETE request to {url} with headers {headers}")
        response = self.session.delete(url, headers=headers, timeout=timeout)
        return self._handle_response(response)

    def _handle_response(self, response):
        self.logger.debug(f"Handling response with status code {response.status_code}")
        if response.status_code >= 200 and response.status_code < 300:
            return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        else:
            self.logger.error(f"Request failed with status code {response.status_code}")
            response.raise_for_status()