# requests

Is a [[python]] library that allow us to make **requests** to a certains [[application programming interface|API]].

## Install

```python
pip install requests
```

## Make a request
We can use the `get` method to make a **GET** request to the API. The `get` method returns a `response` object that contains the response. 

```python
import requests
# Make a request to the API
response = requests.get("api url")
# Get the response in json format
response.json()
```


