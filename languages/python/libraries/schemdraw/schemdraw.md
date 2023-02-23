# [Schemdraw](https://schemdraw.readthedocs.io/en/latest/usage/start.html)

Schemdraw is a [python](/languages/python/python.md) library for **drawing electrical schematics**. It is designed to be easy to use, and to produce high-quality output.

It is based on the [matplotlib](./../matplotlib/matplotlib.md) library, and uses the [LaTeX](/languages/latex/LaTeX.md) typesetting system to produce high-quality output.

## Installation

```bash
pip install schemdraw
```

## [Usage](schemdraw.ipynb)

```python
import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()  # Create a new drawing
d.add(elm.R)  # Add a resistor
d.add(elm.Capacitor)  # Add a capacitor
d.add(elm.Ground)  # Add a ground symbol
d.draw()  # Render the drawing
```


