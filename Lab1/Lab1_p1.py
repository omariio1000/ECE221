import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = x**2
print(f"Value of y: {y}")

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([[1,3,5], [2,4,6], [0,0,1]])
A@B
np.linalg.det(A)
np.linalg.inv(B)
print(f"A: {A}")
print(f"B: {B}")

for k in np.arange(0, 10):
    y = 2**k
    print(y)

k = 0
while k<=10:
    y = 2**k
    k = k+1

response = input('input value for k: ')
k = int(response)
print('k = ', k)
if k < 10:
    y = 2**k
    print('y = ', y)
else:
    print('error')

p = np.array( [1, 2, 3, 4] )
np.roots(p)
x = np.linspace(1, 10, 10)
np.polyval(p, x)

x = np.arange(1, 10.01, 0.01)
y1 = np.exp(x)
y2 = np.exp(2*x)
fig, ax = plt.subplots()
ax.semilogy(x, y1, x, y2)
plt.show()