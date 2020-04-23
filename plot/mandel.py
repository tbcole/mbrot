import numpy as np
import matplotlib.pyplot as plt

def f(z0, c):
    return z0**2+c

def mandelbrot(c:complex, z0=0, tol=100):
    z = f(z0, c)
    for i in range(0, tol):
        z = f(z, c)
        if abs(z) > 2:
            return i
            break
    return tol

#need to define square area of complex points to be tested.
#since Mandelbrot set is defined to be the complex points that f(z) = z^2 + c
#we only want points within the range x=[-2,2], y=[-2,2], c = x +iy, otherwise the point will be ommited

Nx = 4000
Ny = Nx
x = np.linspace(-2, 2, Nx)
y = np.linspace(-2, 2, Ny)
N = Nx*Ny
print(N)

pixval = []
for Y in y:
    for X in x:
        c = X + 1j*Y
        pixval.append(mandelbrot(c))

site = np.arange(0, int(N), 1)
coor = np.zeros((N, 2))
for i in range(0, Nx):
    percent = (i/Nx)*100
    if percent > 74.5 or percent < 75.4:
        print('75%')
    if percent > 49.5 or percent < 50.4:
        print('50%')
    if percent > 24.5 or percent <25.4:
        print('25%')

    for j in range(0, Ny):
        n = i + Nx*j
        coor[n, 0] =  x[i]
        coor[n, 1] = y[j]

plt.scatter(coor[:, 0], coor[:, 1], c=pixval)
