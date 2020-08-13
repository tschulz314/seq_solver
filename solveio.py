#"contains routines to do file I/O for solve.py"

import numpy as np
import os.path

"name of the input directory"
INPUTDIR = "schroedinger_data"
"name of the output directory"
OUTPUTFILE = 'solve.out'


def read_input():
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
    inputfile = os.path.join(INPUTDIR, 'schrodinger.inp') # solve.in
    input = open(inputfile, "r")

    seperatedinput = input.read().splitlines()
    mass = float(seperatedinput[0])
    xlimitsandpoints = seperatedinput[1].split()
    xlimits = np.empty((2, 1))
    xlimits[0] = xlimitsandpoints[0]
    xlimits[1] = xlimitsandpoints[1]
    points = int(xlimitsandpoints[2])
    eigenvalues = [int(seperatedinput[2].split()[0]), int(seperatedinput[2].split()[1])]
    interptype = str(seperatedinput[3])
    numinterp = float(seperatedinput[4])
    """xxandpotentials is created to form an array which connects the x
    coordinates with the assigned potentials.
    """
    xandpot = np.empty((len(seperatedinput) - 5, 2), dtype=float)
    for ii in range(5 ,len(seperatedinput)):
        xxandpotentialunorganized = seperatedinput[ii].split()
        xandpot[ii - 5,0] = xxandpotentialunorganized[0]
        xandpot[ii - 5,1] = xxandpotentialunorganized[1]

    input.close()
    return mass, xlimits, points, eigenvalues, interptype, numinterp, xandpot
# read_input()
