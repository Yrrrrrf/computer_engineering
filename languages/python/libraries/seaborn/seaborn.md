# [Seaborn](https://seaborn.pydata.org/)

Is a [[python]] library for **Data Visualization**. It provides a high-level interface for drawing attractive and informative statistical graphics and is optimized for working with [[pandas]] data structures.

It is built on top of [[numpy]], [[pillow]] and [[matplotlib]].

## Installation
```bash
pip install seaborn
```

## Usage
```python
import seaborn as sns  # This is the main library (it imports matplotlib as well)
import seaborn.apionly as sns  # This module allows you to use seaborn without importing matplotlib
```

## Resources
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Seaborn Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

## Graphics
- [relational plot](replot.ipynb)
    - scatterplot
    - lineplot
- [distribution plot](displot.ipynb)
    - heatmap
    - histogram
    - kdeplot (kernel density estimation plot)
    - ecdfplot (empirical cumulative distribution function plot)
- [categorical plot](catplot.ipynb)
    - stripplot
    - swarmplot
    - boxplot
    - violinplot
    - pointplot
    - barplot
