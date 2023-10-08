import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
import math


n_in = int(input("Enter a number N: "))


T = 1 # period
tmax = 3 * T
omega_0 = 2 * pi / T
N = 2 * n_in + 1 # number of terms in summation is actually 2N + 1
M = 1000 # number of time samples
n = np.arange(1, N+1) # n is 1-D array of size N
a_n = 2 / (1j * n * pi) # a_n is 1-D array of size N
a_n[1::2] = 0 # set even terms = zero
t = np.linspace(0, tmax, M) # t is 1-D array of size M
s = np.array([1 if math.floor(2 * ts) % 2 == 0 else -1 for ts in t])
expon = 1j * omega_0 * n # expon is 1-D array of size N
z = np.exp(np.outer(t, expon)) # z is 2-D array of dimension MxN
# np.outer is the outer product function
x = np.dot(z, a_n) # x is 1-D array of size M
# np.dot is the inner product function
x = 2 * np.real(x)
fig, ax = plt.subplots()
ax.plot(t, s, 'b-', label='original square wave')
ax.plot(t, x, 'r-', label=f'synthesized with N = {N}')

ax.grid()
ax.set_title(f'original and synthesized with N = {N}')
ax.set_xlabel('time, t (s)')
ax.set_ylabel('x(t)')
ax.legend()
plt.show()
