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

#min-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=0)

# plot everything
fig, ax = plt.subplots(1, 2, figsize=(15,3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled Data")
plt.show()

