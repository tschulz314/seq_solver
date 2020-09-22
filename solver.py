"""
Routines for solving the one dimensional schroedinger equation:
"""
import numpy as np
import scipy.linalg as la
import scipy.interpolate


def interpolation(interpoltype, xknown, potknown):
    '''Interpolates the potential for given x and potential refrence values

    Args:
        interpoltype (str): Interpolationtype
                            (linear, cubic spline or polynomial)
        xknown (array): reference x values to interpolate
        potknown (array): reference potential values to interpolate

    Returns:
        pot: function containing the interpolated potential
    '''
    if interpoltype == "linear":
        pot = scipy.interpolate.interp1d(xknown, potknown)
    elif interpoltype == "cspline":
        pot = scipy.interpolate.CubicSpline(xknown, potknown, bc_type='natural')
    else:
        pot = scipy.interpolate.KroghInterpolator(xknown, potknown)
    return pot


def seqsolver(xinfo, pot, mass, neigen):
    """
    calculates the hamiltonian for a given potential

    Args:
        xinfo (array): contains information about the x range
        pot(function): function containing the interpolated potential
        mass (float): mass of the quantum mechanical particle
        neigen (array): cotaines the range of eigenstates to calculate
    Returns:
        energies, x values, wavefuntions and
        delta (axillary size for further calculations)

    """
    npoints = int(xinfo[2])
    xx = np.linspace(xinfo[0], xinfo[1], npoints)
    npoints = xx.shape[0]
    delta = abs(xx[0] - xx[1])
    aa = 1.0 / (mass * delta**2)
    maindi = np.zeros(npoints)
    for ii in range(0, npoints):
        maindi[ii] = aa + pot(xx[ii])
    secdi = (-aa / 2) * np.ones(npoints-1)
    temp = la.eigh_tridiagonal(maindi, secdi, select='i', select_range=neigen)
    energies, wavefunc = temp
    return energies, xx, wavefunc, delta


def normalization(wavefunc, delta):
    """
    Normalizes given wavefunctions

    Args:
        wavefunc (array): contains the wavefuntions
        delta (float): axillary size
    Returns:
        array containing the normalized wavefunctions
    """
    npoints, nfunc = wavefunc.shape
    for ii in range(0, nfunc):
        psisquared = 0
        for jj in range(0, npoints):
            psisquared += np.abs(wavefunc[:, ii][jj])**2
        psisquared *= delta
        wavefunc[:, ii] = wavefunc[:, ii] / np.sqrt(psisquared)
    return wavefunc


def expectedvalue(wavefunc, xx, delta):
    """
    Calculates the expected values and uncertainties
    of x for given wavefunctions

    Args:
        wavefunx (array): contains the wavefuntions
        xx (array): contains the x values
        delta (float): axillary size
    Returns:
        array conatining the expected values and uncertainties
        for the eigenstates
    """
    npoints, nfunc = wavefunc.shape
    expval = np.zeros((nfunc, 2), dtype="float")
    for ii in range(0, nfunc):
        for jj in range(0, npoints):
            expval[ii][0] += np.abs(wavefunc[:, ii][jj])**2 * xx[jj]
            expval[ii][1] += np.abs(wavefunc[:, ii][jj])**2 * xx[jj]**2
        expval[ii][0] *= delta
        expval[ii][1] *= delta
        expval[ii][1] = np.sqrt(np.abs(expval[ii][1]-expval[ii][0]**2))
    return expval
