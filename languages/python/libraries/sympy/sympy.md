# [SymPy](./sympy.ipynb)

Is a [[python]] library for symbolic mathematics. It provides high-performance, easy-to-use data structures and data analysis tools. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible.

**Lambdify**: Is a function that **converts SymPy expressions into pure [[python]] functions**, allowing for [[numpy]] and [[scipy]] to be used for fast numerical computations. It can produce [[tensorflow|TensorFlow]] compatible functions using `lambdify(modules='tensorflow')`.

The `preview()` function can be used to preview the [[LaTeX]] representation of SymPy expressions in the Jupyter notebook.

It also uses [[python]]'s `doctest` module to test the examples in the documentation. This means that the examples are always tested against the latest version of SymPy, and that they can be used as regression tests.

## Installation
```bash
pip install sympy
```

## Usage
```python
import sympy
```

## Resources
- [sympy org](http://sympy.org/en/index.html)
- [SymPy Tutorial](http://docs.sympy.org/latest/tutorial/index.html)
- [a](https://dynamics-and-control.readthedocs.io/en/latest/0_Getting_Started/Notebook%20introduction.html#SymPy)
