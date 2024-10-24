import requests
import logging

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
            self._initialized = True

    def get(self, url, params=None):
        self.logger.debug(f"GET request to {url} with params {params}")
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def post(self, url, data=None, json=None):
        self.logger.debug(f"POST request to {url} with data {data} and json {json}")
        response = requests.post(url, data=data, json=json)
        return self._handle_response(response)

    def put(self, url, data=None, json=None):
        self.logger.debug(f"PUT request to {url} with data {data} and json {json}")
        response = requests.put(url, data=data, json=json)
        return self._handle_response(response)

    def delete(self, url):
        self.logger.debug(f"DELETE request to {url}")
        response = requests.delete(url)
        return self._handle_response(response)

    def _handle_response(self, response):
        self.logger.debug(f"Handling response with status code {response.status_code}")
        if response.status_code >= 200 and response.status_code < 300:
            return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        else:
            self.logger.error(f"Request failed with status code {response.status_code}")
            response.raise_for_status()