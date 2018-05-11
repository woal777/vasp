import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = (x+y) * np.exp(-6.0*(x*x+y*y))

plt.figure()
plt.subplot(211)
plt.pcolor(x, y, z)

plt.colorbar()

plt.title("Sparsely sampled function.")

xnew, ynew = np.mgrid[-1:1:40j, -1:1:40j]
tck = interpolate.bisplrep(x, y, z, s=0)
znew = interpolate.bisplev(xnew[:,0], ynew[0,:], tck)

plt.subplot(212)
plt.pcolor(xnew, ynew, znew)
plt.show()