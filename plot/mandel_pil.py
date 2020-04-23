from PIL import Image
import numpy as np

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

Nx = 512 #num of pixels
Ny = Nx

xmin = -2
xmax = 2
ymin = xmin
ymax = xmax

image = Image.new("RGB", (Nx, Ny))

for y in range(Ny):
    zy = y * (ymax-ymin) / (Ny-1) + ymin
    for x in range(Nx):
        zx = x *(xmax-xmin)/ (Nx-1) + xmin
        C = zx + 1j*zy
        i = mandelbrot(C)
        image.putpixel((x,y), (i%4*64, i%8*32, i%16*16))

image.show()
