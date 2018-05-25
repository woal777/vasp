import macrodensity as md
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

input_file = r'/run/user/1000/gvfs/sftp:host=164.125.41.142,port=7895,user=ksrc5/home/ksrc5/heterojunction/HfO2_TiN/PBE/lvtot/LOCPOT'
lattice_vector = 2.40278

vasp_pot, NGX, NGY, NGZ, Lattice = md.read_vasp_density(input_file)
vector_a, vector_b, vector_c, av, bv, cv = md.matrix_2_abc(Lattice)
resolution_x = vector_a / NGX
resolution_y = vector_b / NGY
resolution_z = vector_c / NGZ
grid_pot, electrons = md.density_2_grid(vasp_pot, NGX, NGY, NGZ)

# POTENTIAL
planar = md.planar_average(grid_pot, NGX, NGY, NGZ)
# MACROSCOPIC AVERAGE
macro = md.macroscopic_average(planar, lattice_vector, resolution_z)
macro2 = md.macroscopic_average(macro, lattice_vector, resolution_z)
x = np.linspace(0, 1, len(planar))
fig, ax1 = plt.subplots(1, 1, sharex=True)

textsize = 22
mpl.rcParams['xtick.labelsize'] = textsize
mpl.rcParams['ytick.labelsize'] = textsize
mpl.rcParams['figure.figsize'] = (10, 6)
ax1.plot(x, planar,label="Planar",lw=3)
ax1.plot(x, macro, label="Macroscopic", lw=3)
ax1.plot(x, macro2, label="Macroscopic2", lw=3)
np.savetxt('/mnt/E_DRIVE/planar.dat', planar)
np.savetxt('/mnt/E_DRIVE/macro2.dat', macro2)

ax1.set_xlim(0, 1)

ax1.grid(True)

ax1.legend(fontsize=22)
plt.show('loc.png')
