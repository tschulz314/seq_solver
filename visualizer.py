"""
Routine to visualize wave functions:
"""
import matplotlib.pyplot as plt
import solver


def wavevisualizer(stretch=1, xlim=None, ylim=None):
    '''
    Visualizes wavefunction.
    Args:

    Returns:

    '''
    xx = solver.hamiltonian()[2]
    wavefunc = solver.normalization()
    energies = solver.solver()[0]
    pot = solver.interpolation()
    expval = solver.expectedvalue()
    npoints, nfunc = wavefunc.shape
    ax1 = plt.subplot(1, 2, 1)
    plt.xlabel("x [Bohr]")
    plt.ylabel("Energy [Hartree]")
    plt.title(r'Potential, eigenstates, $\langle \mathrm{x} \rangle$')
    for ii in range(0, nfunc):
        plt.plot(xx, stretch * wavefunc[:, ii] + energies[ii], color='navy')
        plt.plot(xx, pot(xx), color='black')
        plt.hlines(energies[ii], xx[0], xx[npoints - 1], color='grey')
        plt.plot(expval[ii, 0], energies[ii], 'rx', markersize=8)
    ax2 = plt.subplot(1, 2, 2, sharey=ax1)
    ax2.get_yaxis().set_visible(False)
    plt.xlabel("x [Bohr]")
    plt.title(r'$\sigma_\mathrm{x}$')
    for ii in range(0, nfunc):
        plt.plot(expval[ii, 1], energies[ii], 'x', color='red', markersize=8)
        plt.hlines(energies[ii], 0, expval[nfunc-1, 1] * 1.2, color='grey')
    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim)
    plt.show()
wavevisualizer(stretch=.4, ylim=(0, 3))
