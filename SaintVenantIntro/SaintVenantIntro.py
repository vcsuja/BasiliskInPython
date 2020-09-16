## Python implementation of the Basilisk intro tutorial

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import stream as bas

N = 256
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

#Define adapt criteria
adaptSettings = bas.Adapt()
adaptSettings.maxlevel = 8

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

# Define initial heights
def heightInit(x,y):
    return 0.1 + np.exp(-200.*(x*x + y*y))
def init(i, t):
    bas.h.f = heightInit

def graph(i, t):
  print("t=", t)
  Z = bas.h.f(X, Y)
  plt.cla()
  plt.imshow(Z)
  plt.pause(0.0001)

def end (i,t):
  print ("i = %d,t = %g" % (i, t))

def adapt (i,t):
    adaptSettings.slist = bas.h
    bas.adapt_wavelet(adaptSettings)

# Shift the origin using predefined function
shiftOrigin(-0.5,-0.5,0)

bas.init_grid(N)
imax = 1000

bas.event(init, t=0.)
bas.event(end, i=imax)

plt.ion()
plt.figure()
bas.event(graph, i=range(0, imax, 1))

#Run the simulation
bas.run()
