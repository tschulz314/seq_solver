"""
Routine to visualize wave functions:
"""
import matplotlib.pyplot as plt
import numpy as np


def wavevisualizer(xx, wavefuncs, energies, pot,
                   expval, stretch=1, xlim=None, ylim=None):
    '''
    Visualizes the calculated wavefunctions.
    Args:
        xx (array): contains the x values
        pot (arraayy): contains the interpolated potential
        wavefuncs (array): contains the wavefuntions
        energies (array): contains the energies
        expval: (array): contains the expected values and uncertainties for x
        stretch (float): number for scaling the wavefunctions
        xlim (tuple): the lower and upper limit for the x axis
        ylim (tuple): the lower and upper limit for the y axis
    Returns:
        figures of the wavefunctions, the interpolated potential and the
        energies (1) and the expected values and uncertainties for x (2)
    '''
    npoints, nfunc = wavefuncs.shape
    ax1 = plt.subplot(1, 2, 1)
    plt.xlabel("x [Bohr]")
    plt.ylabel("Energy [Hartree]")
    plt.title(r'Potential, eigenstates, $\langle \mathrm{x} \rangle$')
    for ii in range(0, nfunc):
        if (ii % 2) == 0:
            wcolor = 'navy'
        else:
            wcolor = 'red'
        plt.plot(xx, stretch * wavefuncs[:, ii] + energies[ii], color=wcolor)
        plt.plot(xx, pot, color='black')
        plt.hlines(energies[ii], xx[0], xx[npoints - 1], color='grey')
        plt.plot(expval[ii, 0], energies[ii], 'gx', markersize=8)
    ax2 = plt.subplot(1, 2, 2, sharey=ax1)
    ax2.get_yaxis().set_visible(False)
    plt.xlabel("x [Bohr]")
    plt.title(r'$\sigma_\mathrm{x}$')
    for ii in range(0, nfunc):
        plt.plot(expval[ii, 1], energies[ii], 'x', color='red', markersize=8)
        plt.hlines(energies[ii], 0,
                   expval[np.argmax(expval[:, 1]), 1] * 1.1, color='grey')
    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim)
