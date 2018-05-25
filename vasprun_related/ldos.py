import numpy as np
from pymatgen.io.vasp import Vasprun
from pymatgen.io.vasp.outputs import CompleteDos, Dos
from pymatgen.io.vasp.outputs import Spin, Structure
import os

v = Vasprun('/home/jinho/PycharmProjects/vasp/input/' + 'vasprun.xml')

c = CompleteDos(v.structures, v.tdos, v.pdos)

if __name__ == '__main__':
    s: Structure = c.structure[0]
    arr = [0, 0.05, .1, .15, .2, .25, .31, .37, .46, .52, .57, .63, .68, .74, .78, .84, .9, .95]
    same = [[] for _ in range(len(arr) - 1)]
    for i, k in enumerate(s.frac_coords):
        for j in range(len(arr) - 1):
            if arr[j] <= k[2] < arr[j + 1]:
                same[j].append(i)

    dos = [None for _ in range(len(arr))]
    dos[0] = c.energies - c.efermi
    sites = s.sites
    for ind, i in enumerate(same):
        for j in i:
            if dos[ind + 1] is None:
                dos[ind + 1] = c.get_site_dos(j).get_smeared_densities(sigma=0.05)[Spin.up]
            else:
                dos[ind + 1] += c.get_site_dos(j).get_smeared_densities(sigma=0.05)[Spin.up]

    dos = np.array(dos).transpose()
    np.savetxt('/mnt/E_DRIVE/'+'dos.dat', dos)

