import numpy as np
import pandas as pd
from collections import defaultdict
import time


start = time.time()
def target_mean_v3(data, y_name, x_name):
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

y = np.random.randint(2, size=(5000, 1))
x = np.random.randint(10, size=(5000, 1))
data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])

print(target_mean_v3(data, 'y', 'x'))

end = time.time()
totalTime = end -start 
print(totalTime)