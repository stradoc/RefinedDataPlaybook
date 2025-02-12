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
np.random.seed()
