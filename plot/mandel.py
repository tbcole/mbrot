import numpy as np
import matplotlib.pyplot as plt

def f(z0, c):
    return z0**2+c

#tolerance is set to cover an 8-bit color range (0, 255)
#color of plot will depend on how fast the sequence diverges past 2
#if the c value is in the set, the color will have a pixel value of 0
#and will be black
def mandelbrot(c:complex, z0=0, tol=255):
    z = f(z0, c)
    for i in range(0, tol):
        z = f(z, c)
        if abs(z) > 2:
            return i
            break
    return tol

#need to define square area of complex points to be tested.
#area will be defined by pixels along x and y, A=x*y
#total point will be A
#since Mandelbrot set is defined to be the complex points that f(z) = z^2 + c
#we only want points within the range x=[-2,2], y=[-2,2], c = x +iy, otherwise #the point will be ommited because it is outside of the condition for the set

Nx = 800 #num of pixels
Ny = Nx
x = np.linspace(-2, 0.5, Nx)
y = np.linspace(-1.5, 1.5, Ny)
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
    percent = int((i/Nx)*100)
    if percent == 75:
        print('75%')
    if percent == 50:
        print('50%')
    if percent == 25:
        print('25%')

    for j in range(0, Ny):
        n = i + Nx*j
        coor[n, 0] =  x[i]
        coor[n, 1] = y[j]

plt.scatter(coor[:, 0], coor[:, 1], c=pixval, cmap = 'plasma')
plt.ylim(-1.5, 1.5)
plt.xlim(-2, 0.5)
plt.savefig('mandelbrot.jpg')
plt.show()
