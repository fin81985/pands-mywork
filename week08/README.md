# PANDS Project

## About This Repository

This repository contains an analysis of the renowned Iris dataset, conducted as part of the Programming and Scripting module for the Higher Diploma in Data Analytics at ATU.

Repository Contents

- **README File**: Provides an overview of the repository, including its purpose, contents, and methodology for analyzing Fisher's Iris dataset using Python. It also includes references.

iris.csv: A CSV file containing the dataset, which stores data in a tabular format.

analysis.py: A Python script containing all the code for analyzing the dataset. It includes statistical measures, plots, correlations, and other insights step by step.

summary_variable.txt: A text file summarizing key statistical measures of the dataset in a clear and concise format.

plots.png: A collection of graphical visualizations, including histograms, scatter plots, and a heatmap for the correlation matrix.

Introduction to the Iris Dataset Analysis

The Iris flower dataset, made famous by statistician Ronald Fisher in 1936, is a multivariate dataset widely used in machine learning and statistical analysis. More details can be found on Wikipedia.

Dataset Overview

This dataset contains measurements of three species of the Iris flower:

Setosa

Versicolor

Virginica

It consists of five variables:

Categorical Variable: Species (Setosa, Virginica, Versicolor)

Numerical Variables: Sepal Length, Sepal Width, Petal Length, Petal Width


_Image Source: Giri, A. (2022, June 16)._

Analyzing the Dataset with Python

Python is used for this analysis due to its powerful libraries for data manipulation, statistical operations, and visualization. The following key libraries are imported in analysis.py:

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

The dataset is loaded from a dataset repository:

df = pd.read_csv("https://gist.github.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

Data Exploration and Visualization

Distribution of Iris Species

The dataset is balanced, with 50 samples of each species (Setosa, Versicolor, Virginica), totaling 150 samples.



Summary Statistics



Key observations:

Sepal Length (7.9 cm) has the maximum measurement, while Petal Width (0.10 cm) has the minimum.

Sepals are generally larger than petals.

Petal Length has the highest standard deviation (1.7), indicating greater variation in measurements.

Sepal Width has the lowest standard deviation (0.43), meaning the values are more consistent.

Histogram of Data Distribution



Species-Specific Characteristics

Scatter plots below illustrate how different species vary across feature pairs.







Key Insights

Iris Setosa has shorter and wider sepals and smaller petals compared to other species.

Iris Virginica generally has the longest petals and sepals.

Correlation Analysis

A correlation matrix is used to examine relationships between numerical variables. Correlation values range from -1 to 1:

1: Perfect positive correlation (variables increase together).

0: No correlation.

-1: Perfect negative correlation (one variable increases as the other decreases).



Observations

Strong positive correlation

Petal Length vs Petal Width (0.96): Longer petals tend to be wider.

Sepal Length vs Petal Width (0.82)

Sepal Length vs Petal Length (0.87)

Weak negative correlation

Sepal Length vs Sepal Width (-0.12): Longer sepals do not necessarily mean wider sepals.

Petal Length vs Sepal Width (-0.43)

Sepal Width vs Petal Width (-0.37)

Running the Python Code

To analyze the dataset, first import the required libraries and load the data. Use the following commands for key insights and visualizations:

Basic Statistical Measures

iris_data.min()
iris_data.max()
iris_data.mean()
iris_data.median()
iris_data.std()

Installing Missing Packages

python -m pip install {package_name}

Saving Plots

plt.savefig('plot.png')

Saving Summary to a Text File

numerical_summary = df.describe(include=[np.number])
categorical_summary = df.describe(include=[object])

Generating Visualizations

plt.hist()
plt.scatter()
sns.heatmap()

Computing Correlation Matrix

correlation_matrix = df.corr()

Conclusion

The analysis of the Fisher's Iris dataset provides valuable insights:

Strong positive correlation: Petal length and petal width (0.96) increase together.

Weak negative correlation: Sepal length and sepal width (-0.12) do not exhibit a strong relationship.

Species differentiation:

Iris Setosa has distinct, compact features.

Iris Versicolor and Virginica have overlapping characteristics.

Contribute

If you discover errors or have suggestions for improvements, feel free to submit a pull request.

Author

I am Finian Doonan, currently studying Science in Computing (Data Analytics) at ATU.

References

Iris Dataset - Wikipedia

Seaborn Dataset Repository

Correlation Matrix - Builtin(https://github.com/mwaskom/seaborn-data/blob/master/iris.csv).

```
df = pd.read_csv ("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

```

## Analysis and visualization

![partsofiris](https://ars.els-cdn.com/content/image/3-s2.0-B9780128147610000034-f03-01-9780128147610.jpg)

_Image 3._ by ScienceDirect.com | Science, health and medical journals, full text articles and books. (n.d.).


### Types of iris

The iris data set is balanced, containing an equal number of Iris flower of each species, with 50 samples each (50 Setosa, 50 Versicolor, 50 Virginica). There are 150 Iris flower in total to investigate.

![HistogramIrisSpecies](Figure_1_Iris_Species.png)


### Overview Summary

![Summarydatatable](summary_data_table.png)

In this table is observed that Sepal Length (7.9 cm) has the maximun cm measure and Petal Width the minimum measure (0.10 cm). In general, in these Iris flowers species, Sepal are bigger size than Petal.

In relation to metrics such as mean and standard deviation, there is variability in the results.
For example, Petal Length has the highest standard deviation (1.7), indicating greater dispersion of the data from the mean. Conversely, Sepal Width (0.43) has the lowest standard deviation, meaning the data points are closer to the mean and less dispersed. Petal Length shows the highest variability in flower measurements.

Next, you can observe the following histograms with data distribution of these numerical variables:

![ScreenshotHistogram](Screenshot_Histograms_IrisVariables.png)

### Distinguishing features by species

Below are graphs to show with detail characteristics of each pair of variables taking into account the different iris flower species.

![Scatterplot1](Figure_SepalLength_vs_PetalLength.png)
![Scatterplot2](Figure_SepalLength_vs_PetalWidth.png)
![Scatterplot3](Figure_SepalLength_vs_SepalWidth.png)
![Scatterplot4](Figure_SepalWidth_vs_PetalWidth.png)
![Scatterplot5](Figure_SepalWidth_vs_SepalLength.png)

In this study, the interpretation of result is:

+ Iris Setosa usually shows to have shorter and wider sepals and smaller and shorter petals if is compared to Versicolor and Virginica. 

+ Iris Virginica tends to be the specie with longest and wider petals and sepal.

### Correlation 

In this project is analyzed as well the correlation between each pair of variables , excluding the categorical variable 'Species'.

It is used a correlation matrix, which is defined as a matrix which shows the correlations between all the variables giving us a value between -1 and 1. It helps to summarize all data. For more info:[CorrelationMatrix](https://builtin.com/data-science/correlation-matrix).

The correlation values range between -1 and 1:

+ Value of 1: stronger and perfect positive linear relationship.When one variable increases so does the value of the other.

+ Value of 0:  indicates there is no association between the two variables.

+ Value of -1: indictes negative association. When one variable increases, the other one decreases.

![HeatmapCorrelation](Figure_Heatmap_CorrelationMatrix.png)

In this study, the correlation is interpreted as follows:

- ***Negative and weak correlation***
Sepal length vs sepal width is the weakest and negative linear relationship (-0.12). This means that if the sepal length gets bigger its width won't increase its size too.
Also, petal length vs sepal width (-0.43) and sepal width vs petal width (-037).

- ***Positive and strong correlation***
Petal length vs petal width (0.96) has the strongest and positive correlation. This means that as longer are the petals as longer is its width.
Also, sepal length vs petal width (0.82) and sepal length vs petal length (0.87).

## How to run Python Code

To start using Python programing language for a data analysis, first of all is to import all libraries and loaded the data set as previously detailed. Then you can start using the following codes to explore the data and outcomes some visualizations as .png.

To explore the data and calculate key statistical measures is used the following code:

```
iris_data.min()
iris_data.max()
iris_data.mean()
iris_data.median()
iris_data.std()

```
Importing a package that is not installed:

```
python -m pip install {package_name}
```

To save plots or figures:

``` 
 plt.savefig('.png')
```
To save a summary in a text file:

```
numerical_summary = df.describe(include=[np.number])
categorical_summary = df.describe(include=[object])
```
To plot a visualization:

```
plt.hist()
plt.scatter()
sns.heatmap()
```

To obtain the correlation matrix:

```
correlation_matrix = numeric_df.corr()
```
### Conclusion

To sum up, the analysis of Fisher's Iris data set reveals key insights:

- Strong and positive correlation between petal dimensions: Petal length and petal width (0.96). It  means that as longer are the petals on Iris flowers as much is increasing the petal wide.

- Weak and negative correlation with sepal width: sepal length and sepal width (-0.12). It is not matter how much bigger or length has the iris sepal , Its wide won't increase its size too. It is not correlated.

- Species differentation: Iris setosa displays more distinct measurements compared to Iris Versicolor and Virginica. Iris Setosa tends to have shorter and wider sepals. Also, smaller and shorter petals.
Iris Versicolor and Virginica shows some overlap in some scatter plots. They are more coincidences.


## Contribute

You can submit a pull request regarding my code if you discover an error or if It should be updated.


## Author 
I am Finian Doonan and I am currently studying Science in Computing in Data Analytics at [ATU](https://www.atu.ie/).


## URL References:

-