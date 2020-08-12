## Python implementation of the Baslisk test case stream.c
## Studies the merger of two vortices

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import stream as bas
from PIL import Image

N = 256
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

#Visualization
images = []
cmap = plt.cm.jet
norm = plt.Normalize(vmin=0, vmax=1)

# Define shiftOrigin function
def shiftOrigin(x,y,z):
    global X
    global Y

    p = bas._origin()
    p.x = x
    p.y = y
    p.z = z
    bas.origin(p)
    X = X + x
    Y = Y + y

# Define initial vorticity field
def vortexInit(x,y):
    dd = 0.1
    return np.exp(-(np.square(x-dd)+np.square(y))/(dd/10.)) + np.exp(-(np.square(x+dd)+np.square(y))/(dd/10.))
def init(i, t):
    bas.omega.f = vortexInit

# Use matplotlib to visualize the generated vorticity field
def graph(i, t):
    print ("t=",t)
    Z = bas.omega.f(X,Y)
    images.append(Image.fromarray(np.uint8(cmap(Z)*255)))
    plt.cla()
    plt.imshow(Z)
    plt.pause(0.010)


# Shift the origin using predefined function
shiftOrigin(-0.5,-0.5,0)
# Initialize grid
bas.init_grid(N)

#Register the initial condition and graph the function
bas.event(init, t=0.)
plt.ion()
plt.figure()
bas.event(graph, t=np.arange(0,30,0.1))

#Run the simulation
bas.run()

#Save the gif file:
images[0].save('VortexMerger.gif',save_all=True, append_images=images[1:], optimize=False, duration=5, loop=0)
