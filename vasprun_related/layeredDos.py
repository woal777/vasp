import numpy as np
from pymatgen.io.vasp import Vasprun
from pymatgen.io.vasp.outputs import CompleteDos, Dos
from pymatgen.io.vasp.outputs import Spin, Structure
import os

v = Vasprun(os.path.abspath(os.curdir) + '/vasprun.xml')

c = CompleteDos(v.structures, v.tdos, v.pdos)


if __name__ == '__main__':
    s: Structure = c.structure[0]
    z = []
    for i in s.frac_coords:
        b = True
        for j in z:
            if abs(j - i[2]) < 1e-2:
                b = False
        if b:
            z.append(i[2])
    z = sorted(z)
    same = [[] for _ in range(len(z))]
    for k, i in enumerate(s.frac_coords):
        for ind, j in enumerate(z):
            if abs(i[2] - j) < 1e-2:
                same[ind].append(k)
    dos = [None for _ in range(len(z))]
    pdos = [None for _ in range(len(z))]
    sites = s.sites
    for ind, i in enumerate(same):
        for j in i:
            if dos[ind] is None:
                dos[ind] = c.get_site_dos(sites[j]).densities[Spin.up]
                pdos[ind] = c.get_site_dos(sites[j])
            else:
                dos[ind] += c.get_site_dos(sites[j]).densities[Spin.up]
                pdos[ind].__add__(c.get_site_dos(sites[j]))
    dos = np.array(dos).transpose()
    with open('dos.dat', 'w') as f:
        for ind, i in enumerate(c.energies):
            f.write('%f\t' % (i - c.efermi))
            for j in dos[ind][:-1]:
                f.write('%f\t' % j)
            f.write('%f' % dos[ind][-1])
f.write('\n')