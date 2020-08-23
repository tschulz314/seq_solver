# contains routines to do file I/O for solve.py

import os.path
import numpy as np


def read_input(inputdir):
    """Reads in the data for a given quantum system.

    Args:
        directory: Directory containing the file with the QM-system details.

    Returns:
        Value (mass, points, numberinterpolation) the mass,
        number of points in-between the x-limits
        and the number of interpolation points.
        Tuple ( )
        Array (xx, potential) the x-coordinates and the potential.
        String (InterpType) the type of interpolation.
    """
    inputfile = os.path.join(inputdir, 'schrodinger.inp')
    input = open(inputfile, "r")
    seperatedinput = input.read().splitlines()
    mass = float(seperatedinput[0])
    xinfo = seperatedinput[1].split()
    xinfo = list(map(float, xinfo))
    eigenvalues = seperatedinput[2].split()
    eigenvalues = list(map(int, eigenvalues))
    interptype = str(seperatedinput[3])
    numinterp = float(seperatedinput[4])
    xandpot = np.empty((len(seperatedinput) - 5, 2), dtype=float)
    for ii in range(5, len(seperatedinput)):
        xxandpotentialunorganized = seperatedinput[ii].split()
        xandpot[ii - 5, 0] = xxandpotentialunorganized[0]
        xandpot[ii - 5, 1] = xxandpotentialunorganized[1]
    input.close()
    return mass, xinfo, eigenvalues, interptype, numinterp, xandpot
# read_input("schroedinger_data")
