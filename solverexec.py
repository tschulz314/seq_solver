"""
Executable python script for solving the one dimensinal schroedinger equation:
"""

import argparse
import schrodinger_solver.solveio as solveio
import schrodinger_solver.solver as solver

_DESCRIPTION = 'Script for solving the schrodinger equation'


def main():
    """
    Main function for solving the schroedinger equation.

    Args:
        inputdir (str): name of the input directory (for parsing)

    Returns:
        the files energies.dat, potential.dat, wavefuncs.dat, expvalues.dat
        containing the calculated results
    """
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory to "schrodinger.inp" (default: .)'
    parser.add_argument('-d', '--directory', default='.',
                        metavar='DIR', help=msg)
    args = parser.parse_args()
    temp = solveio.read_input(args.directory)
    interpoltype = temp[3]
    xknown = temp[5][:, 0]
    potknown = temp[5][:, 1]
    pot = solver.interpolation(interpoltype, xknown, potknown)
    xinfo = temp[1]
    mass = temp[0]
    eigenrange = temp[2][0] - 1, temp[2][1] - 1
    catcher = solver.seqsolver(xinfo, pot, mass, eigenrange)
    energies, xx, wavefunc, delta = catcher
    wavefunc = solver.normalization(wavefunc, delta)
    expval = solver.expectedvalue(wavefunc, xx, delta)
    solveio.write_output(energies, xx, wavefunc, expval, pot, args.directory)


if __name__ == "__main__":
    main()
