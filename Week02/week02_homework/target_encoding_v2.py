
import numpy as np
import pandas as pd
import time

start = time.time()
def target_mean_v2(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    value_dict = dict()
    count_dict = dict()
    for i in range(data.shape[0]):
        if data.loc[i, x_name] not in value_dict.keys():
            value_dict[data.loc[i, x_name]] = data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] = 1
        else:
            value_dict[data.loc[i, x_name]] += data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] += 1
    for i in range(data.shape[0]):
        result[i] = (value_dict[data.loc[i, x_name]] - data.loc[i, y_name]) / (count_dict[data.loc[i, x_name]] - 1)
    return result

y = np.random.randint(2, size=(5000, 1))
x = np.random.randint(10, size=(5000, 1))
data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])

print(target_mean_v2(data, 'y', 'x'))
end = time.time()
totalTime = end - start
print(totalTime)