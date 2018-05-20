import numpy as np
from pymatgen.io.vasp import Chgcar
import matplotlib.pyplot as plt


def interpolate(arr: np.ndarray):
    new = np.zeros([r * 2 for r in arr.shape])
    new[0::2, 0::2] = arr
    for n in range(arr.shape[1] - 1):
        new[:, 2 * n + 1] = (new[:, 2 * n] + new[:, 2 * n + 2]) / 2
    for n in range(arr.shape[0] - 1):
        new[2 * n + 1, :] = (new[2 * n, :] + new[2 * n + 2, :]) / 2
    return new


chg = Chgcar.from_file('CHGCAR')

fig = plt.figure(figsize=(10, 10))
values = chg.data['total'][0]
values = interpolate(values)
values = interpolate(values)
values = interpolate(values)
plt.pcolor(values)
plt.savefig(filename='chg.png')
