from target_encoding_v4 import target_mean_v4
import numpy as np
import pandas as pd
import time

start = time.time()
y = np.random.randint(2, size=(5000, 1))
x = np.random.randint(10, size=(5000, 1))
data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
print(target_mean_v4(data, 'y','x'))

end = time.time()
totalTime = end - start
print(end -start)