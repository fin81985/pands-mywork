# Analysis of Iris Dataset
# Author: Finian Doonan

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("https://gist.github.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
df.to_csv("iris.csv", index=False)

# Display first 5 rows
print(df.head())

# Save summaries to a text file
numerical_summary = df.describe(include=[np.number])
categorical_summary = df.describe(include=[object])

with open('Summary_variable.txt', 'w') as file:
    file.write("Numerical Variables Summary:\n")
    file.write(numerical_summary.to_string())
    file.write("\n\nCategorical Variables Summary:\n")
    file.write(categorical_summary.to_string())

# Generate histograms
df.hist(figsize=(10, 8), color='purple', edgecolor='black')
plt.savefig('histograms.png')
plt.show()



# Display data types
df.dtypes

# Display first few rows
df.head()

# Display dataset shape
df.shape
