import numpy as np
from pymatgen.io.vasp import Structure, Outcar

s: Structure = Structure.from_file('POSCAR')
out = Outcar('OUTCAR')
pDown: Structure = Structure.from_file('POSCAR')
pOrigin: Structure = Structure.from_file('test_POSCAR/POSCAR')
e = 1.60217646e-19
v = s.volume
pol = np.zeros(3)
b = out.born

for i in range(len(b)):
    pol += np.dot(b[i], pDown.cart_coords[i] - pOrigin.cart_coords[i])

print(pol * e / v * 1e+22)  # uC/cm^2
