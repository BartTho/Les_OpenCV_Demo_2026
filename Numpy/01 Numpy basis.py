# pip install numpy
import numpy as np

mijn_lijst = [1, 2, 3, 4, 5]
arr = np.array(mijn_lijst)

print(arr)
print(arr.min())
print(arr.max())

print(np.zeros((5,5)))
print(np.ones((5,5))*255)