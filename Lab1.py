import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter a number N"))
a = np.zeros(n)

for i in range(n):
    if (i % 2 == 1):
        a[i] = 2/(n * np.pi)