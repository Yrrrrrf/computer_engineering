# [Selenium](http://selenium-python.readthedocs.io/index.html)

Is a [[python]] library that allows you to automate the browser. It can be used to test the application, or to automate the process of filling forms, or to automate the process of downloading files.

## Installation

```bash
pip install selenium
```

## [Usage](selenium.ipynb)
```python
from selenium import webdriver  # Import the webdriver to control the browser
from selenium.webdriver.common.keys import Keys  # Import the keys that we can use to interact with the browser

driver = webdriver.Firefox()  # Create a new instance of the Firefox driver
driver.get("http://www.python.org")  # Go to the python website
assert "Python" in driver.title  # Check if the title of the page contains the word "Python"
elem = driver.find_element_by_name("q")  # Find the search box
elem.send_keys("pycon")  # Type "pycon" in the search box
elem.send_keys(Keys.RETURN)  # Press the enter key
assert "No results found." not in driver.page_source  # Check if the page source contains the word "No results found."
driver.close()  # Close the browser
```

### References
- [Selenium with Python](http://selenium-python.readthedocs.io/index.html)
- [Selenium with Python - Tutorial](https://www.guru99.com/selenium-tutorial.html)
