import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Load the dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(url)

# Summary statistics
stats = df.describe().T[['mean', 'min', 'max', 'std']]
stats['median'] = df.median(numeric_only=True)
print(stats)

# Histogram plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for idx, feature in enumerate(features):
    sns.histplot(df, x=feature, bins=20, kde=True, hue="species", multiple="stack", edgecolor='black', alpha=0.7, ax=axes[idx])
    axes[idx].axvline(df[feature].mean(), color='r', linestyle='dashed', linewidth=1.5, label="Mean")
    axes[idx].set_title(feature, fontsize=14)
    axes[idx].set_xlabel("Value (mm)", fontsize=12)
    axes[idx].set_ylabel("Frequency", fontsize=12)
    axes[idx].legend()

plt.tight_layout()
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 6))
colors = {'setosa': 'r', 'versicolor': 'g', 'virginica': 'b'}
for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], color=color, label=species, alpha=0.7, s=80)
plt.xlabel("Sepal Length (mm)", fontsize=12)
plt.ylabel("Petal Length (mm)", fontsize=12)
plt.title("Scatter Plot of Sepal Length vs Petal Length", fontsize=14)
plt.legend()
plt.show()

# Linear Regression
X = df[['sepal_length']]
y = df['petal_length']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(8, 6))
sns.regplot(x='sepal_length', y='petal_length', data=df, scatter_kws={'alpha':0.7, 's':80}, line_kws={'color':'black'})
plt.xlabel("Sepal Length (mm)", fontsize=12)
plt.ylabel("Petal Length (mm)", fontsize=12)
plt.title("Regression: Sepal Length vs Petal Length", fontsize=14)
plt.show()

# Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='petal_length', data=df, palette=colors)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Length (mm)", fontsize=12)
plt.title("Box Plot of Petal Lengths for Each Species", fontsize=14)
plt.show()

# Heatmap of feature correlations
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, square=True)
plt.title("Correlation Heatmap of Iris Features", fontsize=14)
plt.show()

# Pairplot
sns.pairplot(df, hue="species", diag_kind="kde", palette=colors, height=2.5, corner=True)
plt.show()
