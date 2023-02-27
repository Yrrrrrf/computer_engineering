# [Seaborn](https://seaborn.pydata.org/)

Write by Michael Waskom. Is a [[python]] library for **Data Visualization**. It provides a high-level interface for drawing attractive and informative statistical graphics and is optimized for working with [[pandas]] data structures.

It is built on top of [[numpy]], [[pillow]] and [[matplotlib]].

## Installation
```bash
pip install seaborn
```

## [Usage](seaborn.ipynb)
```python
import seaborn as sns  # This is the main library (it imports matplotlib as well)
import seaborn.apionly as sns  # This module allows you to use seaborn without importing matplotlib
```

The main function is `sns.set()`. It sets the aesthetic parameters in one step. It is equivalent to calling `sns.set_style()`, `sns.set_context()`, `sns.set_palette()` and `sns.set_color_codes()`.
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

![seaborn cheatsheet](seaborn%20cheatsheets.png)


## Resources
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Seaborn Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)
