# [Dask](https://www.dask.org/)

Is a [[python]] library that allows you to scale your workflows from your laptop to a cluster with minimal code changes. Dask is a flexible [[parallel computing]] library for **[[analytic computing]]**.

Dask makes it easy to scale the Python libraries that you know and love like [[numpy|NumPy]], [[pandas]], and [[scikit-learn]].

Dask is composed of two components:
- Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that extend common interfaces like NumPy, Pandas, or Python iterators to larger-than-memory or distributed environments. These parallel collections run on top of the dynamic task schedulers.

## Installation

```bash
pip install dask
```

## Usage
    
```python
import dask.array as da  # parallel NumPy
import dask.dataframe as dd  # parallel Pandas
import dask.bag as db  # parallel python collections
```

### Example

```python
import dask.bag as db
b = db.from_sequence(range(1000), npartitions=10)
def inc(x):
return x + 1
c = b.map(inc)
c.compute()
```

