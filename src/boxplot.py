from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# you can save the boxplot...

import matplotlib.pyplot as plt
import os

# Ensure the 'figs' directory exists
if not os.path.exists('figs'):
    os.makedirs('figs')

# Create a box plot for 'MedInc' (Median Income)
plt.figure(figsize=(8, 6))
df['MedInc'].plot(kind='box')
plt.title('Box plot of Median Income')
plt.ylabel('Median Income')

# Save the figure
plt.savefig('figs/boxplot.png')
plt.show()