import numpy as np
b = np.arange(12).reshape(3,4)
print(b)
# suma całej macierzy
# print(b.sum())
# suma każdej z kolumn
print(b.sum(axis=0))