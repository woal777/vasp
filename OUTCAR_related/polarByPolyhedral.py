import numpy as np
from pymatgen.io.vasp import Structure, Outcar

s: Structure = Structure.from_file('POSCAR')
out = Outcar('OUTCAR')
e = 1.60217646e-19
v = s.volume
pol = np.zeros(3)

for j in range(4):
    result = np.zeros(3)
    for i in s.get_all_neighbors(2.5)[j]:
        result += i[0].coords
    diff = result / 7 - s.sites[j].coords
    pol += np.inner(out.born[j], diff)

print(pol * e / v * 1e+22)  # uC/cm^2
