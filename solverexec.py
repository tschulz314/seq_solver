"""
Executable python script for solving the one dimensinal schroedinger equation:
"""
import solveio
import solver


def main(inputdir="testdata/assymetric_well.inp", outputfiles=True):
    """
    Main function for solving the schroedinger equation
    """
    temp = solveio.read_input(inputdir)
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
    if outputfiles is True:
        solveio.write_output(energies, xx, wavefunc, expval, pot)
    else:
        return xx, pot, expval


if __name__ == "__main__":
    main()
