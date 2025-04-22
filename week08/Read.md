
# Iris Dataset Analysis

**Module:** Principles of Data Analytics  
**Author:** Finian Doonan

This project explores the classic [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) using Python libraries such as [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), and [Scikit-learn](https://scikit-learn.org/). The aim is to perform data exploration, statistical analysis, and simple machine learning modeling.

---

##  Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
```

- **NumPy**: Fundamental package for numerical computations in Python. [Documentation](https://numpy.org/doc/)
- **Pandas**: Data manipulation and analysis library. [Documentation](https://pandas.pydata.org/docs/)
- **Matplotlib**: Plotting library for creating static, animated, and interactive visualizations. [Documentation](https://matplotlib.org/stable/contents.html)
- **Seaborn**: Statistical data visualization built on top of Matplotlib. [Documentation](https://seaborn.pydata.org/)
- **Scikit-learn**: Machine learning library for Python. [Documentation](https://scikit-learn.org/stable/documentation.html)

---

##  Task 1: Source the Dataset

- **Data Source**: Loaded directly from a public CSV hosted on GitHub.
- **Alternative**: The `load_iris()` function in `sklearn.datasets` returns a dictionary-like object that includes features, labels, and metadata. [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)

---

##  Task 2: Explore the Data Structure

- **Shape**: `(150, 5)` — 150 samples and 5 columns.
- **Columns**: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species`
- **Classes**: `setosa`, `versicolor`, `virginica`
- **Data Inspection**: Utilized `.head()`, `.tail()`, `.keys()`, and `.describe()` to understand data structure.

[Exploratory Data Analysis Reference](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)

---

##  Task 3: Summarize the Data

Calculated for each feature:

- Mean
- Minimum
- Maximum
- Standard Deviation
- Median

Displayed using Pandas `.describe()` and extended with `.median()`.

---

##  Task 4: Visualize Features

- Plotted **histograms** for all four features using Matplotlib.
- Each plot is labeled with title, x-axis (in mm), and frequency on y-axis.

[Matplotlib Tutorial](https://www.geeksforgeeks.org/matplotlib-tutorial/)

---

##  Task 5: Investigate Relationships

- Created **scatter plot** between `sepal_length` and `petal_length`.
- Points are color coded by class: Setosa (red), Versicolor (blue), Virginica (cyan).

---

## Task 6: Analyze Relationship

- Used `numpy.polyfit` to fit and a **regression line** on the scatter plot.
- Demonstrates linear correlation between the selected features.

[Linear Regression Example](https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_lm/)

---

## Task 7: Analyze Class Distributions

- **Box plots** were created to show the distribution of `petal_length` across each class.
- This highlights differences in median, spread, and potential outliers.

---

## Task 8: Compute Correlations

- A **correlation matrix** was calculated using `DataFrame.corr()`.
- Displayed as a **Seaborn heatmap** with annotations to show correlation strength between features.

---

## Task 9: Simple Linear Regression

- Fitted a **linear regression model** (`LinearRegression`) for `sepal_length` vs `petal_length`.
- Calculated **R² (coefficient of determination)** using `r2_score`.
- Annotated the scatter plot with the R² value for interpretability.

[ML Model Guide](https://www.codeunderscored.com/building-your-first-machine-learning-model-using-iris-dataset/)

---

## Task 10: Too Many Features

- Used `seaborn.pairplot()` to plot pairwise relationships between all features.
- **Explanation**: A pairplot shows scatter plots for every pair of features, histograms for individual features, and class-based coloring to help visualize class separability and feature correlation.

---

## Conclusion

This project demonstrates foundational data analysis skills:

- Data loading and exploration
- Summary statistics and visualization
- Basic modeling and evaluation
- Insights through visual storytelling
