# Experiments with data cleaning techniques and exponentiality.

import pandas as pd
import numpy as np

# for box-cut transformation
from scipy import stats

# for scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# set seed for reproducibility
np.random.seed(0)

# generate data points
original_data = np.random.exponential(size=1000)

# min-max scale the data between 0 and 1
# scaling allows the machine to use the data properly.
# recognizing which values are more important or less important
# basically standardizing units.
scaled_data = minmax_scaling(original_data, columns=0)

# plot everything
fig, ax = plt.subplots(1, 2, figsize=(15,3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled Data")
plt.show()

# normalize the exponential data with boxcox
# normalization prevents outliers from dominating the dataset
# useful when outliers dominate & the actual dataset has a normal distribution
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")
plt.show()