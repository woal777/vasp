import pymatgen.command_line.gulp_caller as gulp
from pymatgen.command_line.gulp_caller import Structure
from pymatgen.core.sites import Specie


def make(filename, st):
    gio = gulp.GulpIO()
    gc = gulp.GulpCaller('gulp')
    gin = gio.buckingham_input(
        st, ('optimise', 'conp', 'qok'))
    gout = gc.run(gin)
    energy = gio.get_energy(gout)
    relax_structure = gio.get_relaxed_structure(gout)
    print(filename, energy)
    relax_structure.to('POSCAR', filename=filename)


if __name__ == "__main__":
    n = 0
    for i in range(4, 8):
        for j in range(7, i, -1):
            n += 1
            s: Structure = Structure.from_file('POSCAR')
            s.replace(i, species=Specie('Gd'))
            s.replace(j, species=Specie('Gd'))
            make('%02d' % n, s)
