import pytest
import requests
from unittest.mock import patch
from fetchio.http import Http

@patch('requests.get')
def test_http_get(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    mock_response.headers = {'Content-Type': 'application/json'}

    http = Http()
    response = http.get("http://example.com")

    assert response == {"key": "value"}
    mock_get.assert_called_once_with("http://example.com", params=None)

@patch('requests.post')
def test_http_post(mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 201
    mock_response.json.return_value = {"key": "value"}
    mock_response.headers = {'Content-Type': 'application/json'}

    http = Http()
    response = http.post("http://example.com", json={"data": "test"})

    assert response == {"key": "value"}
    mock_post.assert_called_once_with("http://example.com", data=None, json={"data": "test"})

@patch('requests.put')
def test_http_put(mock_put):
    mock_response = mock_put.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    mock_response.headers = {'Content-Type': 'application/json'}

    http = Http()
    response = http.put("http://example.com", json={"data": "test"})

    assert response == {"key": "value"}
    mock_put.assert_called_once_with("http://example.com", data=None, json={"data": "test"})

@patch('requests.delete')
def test_http_delete(mock_delete):
    mock_response = mock_delete.return_value
    mock_response.status_code = 204
    mock_response.text = "Deleted"

    http = Http()
    response = http.delete("http://example.com")

    assert response == "Deleted"
    mock_delete.assert_called_once_with("http://example.com")