# Virtual Environment

**(.venv) files**

Is a tool to create **isolated** Python environments.

### Create a virtual environment
1. Create .venv folder
```python
py -m venv .venv  # Call venv module and create .venv folder
```
2. Activate .venv
```python
.venv\Scripts\activate  # Activate .venv
.venv\Scripts\deactivate  # Deactivate .venv
```

### Create an alias
This makes easier to activate .venv
```python
alias venv=.venv\Scripts\activate  # Create an alias that activate .venv
```

### Install packages
```python
pip install <package>  # Install a package in the current .venv
pip freeze  # List all modules installed in the current .venv
pip freeze > requirements.txt  # Create a requirements.txt file with all modules installed in the current .venv 
pip install -r requirements.txt  # Install all packages in requirements.txt
```
