
# 📊 Project 2025 – Iris Dataset Analysis  
**Module:** Programming and Scripting  
**Author:** Finian Doonan  

---

## 🧠 Introduction

The **Iris dataset** is a classic in the field of statistics and machine learning. Introduced by Ronald A. Fisher in 1936, it contains measurements of 150 iris flowers across three species: *setosa*, *versicolor*, and *virginica*. Each sample includes four numerical features: sepal length, sepal width, petal length, and petal width.

This project uses Python and several data science libraries to:
- Explore the dataset
- Generate statistical summaries
- Create visualizations
- Perform linear regression
- Examine feature correlations

---

## 🛠️ Libraries Used

- **NumPy**: Numerical operations
- **Pandas**: Data manipulation
- **Scikit-learn**: ML utilities and datasets
- **Matplotlib**: Plotting library
- **Seaborn**: Statistical data visualization

---

## 📥 Loading the Dataset

```python
df = pd.read_csv("iris_dataset/iris.data")
```

The dataset is loaded into a Pandas DataFrame and column names are renamed for clarity:
```python
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
```

---

## 📊 Summary Statistics

Descriptive statistics such as **mean, median, min, max, and standard deviation** were calculated for each feature.  
Example output:
```
              mean   min   max    std   median
sepal_length  5.84  4.3   7.9   0.83    5.8
petal_length  3.77  1.0   6.9   1.76    4.4
```

This gives a quick understanding of the dataset’s distribution and spread.

---

## 📈 Visualizations

### 1. **Histograms**
Histograms show the distribution of each feature using values generated from a normal distribution with the same mean and standard deviation as the actual dataset.

### 2. **Scatter Plot: Sepal Length vs Petal Length**
Using randomly assigned class labels, a scatter plot reveals patterns between two features. Different classes are color-coded to show separation between species.

### 3. **Linear Regression Line**
A regression line was fitted to the above scatter plot using `numpy.polyfit`. This helps visualize the **linear relationship** between sepal length and petal length.

### 4. **Box Plots**
Box plots show the spread and central tendencies of petal lengths across the three classes, highlighting medians and potential outliers.

### 5. **Heatmap**
A **correlation matrix** visualized via a heatmap highlights the relationships between features. For example, petal length and petal width show a strong positive correlation.

### 6. **Pair Plot**
A pair plot provides scatter plots for all feature combinations, colored by species. It reveals clusters and relationships useful for classification tasks.

---

## 📌 Key Observations

- **Petal dimensions** are more effective for distinguishing between species than sepal dimensions.
- The **Setosa** class is well-separated from the other two, which are more closely aligned.
- Strong correlation exists between **petal length** and **petal width**, suggesting redundancy in features.

---

## 📚 References

- [UCI Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)
- [NumPy Documentation](https://numpy.org/doc/stable/user/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)
- [Matplotlib Users Guide](https://matplotlib.org/stable/users/index.html)
- [Seaborn Documentation](https://seaborn.pydata.org/index.html)

---

## ✅ Conclusion

This project provided an insightful exploration of the Iris dataset, showcasing key Python libraries for data science. Through visualization and simple statistical analysis, important patterns in the data were uncovered. Future work could include applying classification models like **KNN or SVM** to predict species based on measurements.
