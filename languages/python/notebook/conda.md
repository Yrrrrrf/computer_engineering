# [Conda](https://docs.conda.io/en/latest/)
Is a [[python]] package manager that allow us to create [[venv|virtual environments]].

## Create a conda environment
1. Create `conda` environment
```python
conda create --name <env_name>  # Create a conda environment
```

2. Activate `conda` environment
```python
conda activate <env_name>  # Activate conda environment
conda deactivate  # Deactivate conda environment
```

### Install packages
```python
conda install <package>  # Install a package in the current conda environment
conda list  # List all modules installed in the current conda environment
```

### Manage conda environment
There are some commands to manage conda environments.
```python
conda env create -f environment.yml  # Create a new environment with the packages in the `environment.yml` file
conda env export > environment.yml  # Create a `environment.yml` file with the packages in the current environment
conda env remove --name <env_name>  # Remove a conda environment
conda env update --file environment.yml --prune  # Update the environment with the packages in the `environment.yml` file
```

## Conda channels
Conda channels are the locations where the packages are stored. There are two types of channels:
- `defaults`: The default channel where the packages are stored.
- `conda-forge`: The channel where the packages are stored.
```python
conda config --add channels <channel_name>  # add a new channel
conda config --remove channels <channel_name>  # remove a channel
```

### Conda environment file
The `environment.yml` file is a file that contains all the packages installed in a conda environment. It is used to create a new environment with the same packages installed in the current environment.
