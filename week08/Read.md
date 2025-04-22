
# Iris Dataset Analysis

This project explores the famous Iris dataset using Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn. The aim is to perform data exploration, statistical analysis, and simple machine learning modeling.

---

## Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
```

---

## Task 1: Source the Dataset

- **Data Source**: Loaded directly from a public CSV hosted on GitHub.
- **Explanation of `load_iris()`**: The `load_iris()` function in `sklearn.datasets` returns a dictionary-like object that includes features, labels, and metadata. However, for this project, the dataset is loaded from a CSV link instead.

---

## Task 2: Explore the Data Structure

- Shape: `(150, 5)` — 150 samples and 5 columns.
- Columns: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species`
- Classes: `setosa`, `versicolor`, `virginica`
- Data inspection: `.head()`, `.tail()`, `.keys()`, and `.describe()` used to understand data structure.

---

## Task 3: Summarize the Data

Calculated for each feature:
- Mean
- Minimum
- Maximum
- Standard Deviation
- Median

Displayed using Pandas `.describe()` and extended with `.median()`.

---

## Task 4: Visualize Features

- Plotted **histograms** for all four features using Matplotlib.
- Each plot is labeled with title, x-axis (in mm), and frequency on y-axis.

---

## Task 5: Investigate Relationships

- Created **scatter plot** between `sepal_length` and `petal_length`.
- Points are color-coded by class: Setosa (red), Versicolor (blue), Virginica (cyan).

---

## Task 6: Analyze Relationship

- Used `numpy.polyfit` to fit and overlay a **regression line** on the scatter plot.
- Demonstrates linear correlation between the selected features.

---

## Task 7: Analyze Class Distributions

- **Box plots** were created to show the distribution of `petal_length` across each class.
- This highlights differences in median, spread, and potential outliers.

---

##  Task 8: Compute Correlations

- A **correlation matrix** was calculated using `DataFrame.corr()`.
- Displayed as a **Seaborn heatmap** with annotations to show correlation strength between features.

---

## Task 9: Simple Linear Regression

- Fitted a **linear regression model** (`LinearRegression`) for `sepal_length` vs `petal_length`.
- Calculated **R² (coefficient of determination)** using `r2_score`.
- Annotated the scatter plot with the R² value for interpretability.

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
