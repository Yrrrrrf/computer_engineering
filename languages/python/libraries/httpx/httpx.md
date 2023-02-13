# [HTTPX](https://www.python-httpx.org/)

Is a **next generation HTTP client** for [Python](/languages/python/python.md) 3.6+.

Is really simillar to [requests](./../requests.md) module but with a better performance. Also, it is a sync and async client.
The [FastAPI](./../fast_api/FastAPI.md) framework recommends to use this module instead of [requests](./../requests.md).

## Installation

```bash
pip install httpx
```

## [Usage](httpx.ipynb)
http request and response.
```python
import httpx

# request
response = httpx.get("https://httpbin.org/get")  # get the response
response.status_code  # 200
response.text  # the response body
response.json()  # the response body as a dict

# response
response = httpx.Response(200, json={"hello": "world"})
response.status_code  # 200
response.text  # '{"hello": "world"}'
response.json()  # {'hello': 'world'}
```
