import numpy as np
import pandas as pd
from collections import defaultdict

def target_mean_v4(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    value_dict = defaultdict(int)
    count_dict = defaultdict(int)
    x = data[x_name].values
    y = data[y_name].values
    for i in range(x.shape[0]):
        value_dict[x[i]] += y[i]
        count_dict[x[i]] += 1
    for i in range(x.shape[0]):
        result[i] = (value_dict[x[i]] - y[i]) / (count_dict[x[i]] - 1)
    return result

