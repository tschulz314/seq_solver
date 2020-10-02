"""
Executable python script for visualizing the results of the one dimensional
schroedinger equation.
"""
import argparse
import schrodinger_solver.solveio as solveio
import schrodinger_solver.visualizer as visualizer
import matplotlib.pyplot as plt
import os.path

_DESCRIPTION = 'Script for solving the schrodinger equation'


def main():
    """
    Main function for visualizing the results of the one dimensional
    schroedinger equation.

    Args:
        inputdir (str): name of the input directory (for parsing)
        stretch (float): number for scaling the wavefunctions
        xlimits (tuple): the lower and upper limit for the x axis
        ylimits (tuple): the lower and upper limit for the y axis
        command (str): command whether to print the figures as PDF

    Returns:
        figure containing the wavefunctions and expexted value and
        uncertainties for x
    """
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = '''directory containing the files energies.dat,
    potential.dat, wavefuncs.dat, expvalues.dat (default: .)'''
    parser.add_argument('-d', '--inputdir', default='.',
                        metavar='DIR', help=msg)
    msg = 'Float used to scale the wave functions (default: 1.0)'
    parser.add_argument('--stretch', type=float, default='1.0',
                        metavar='NUM', help=msg)
    msg = '''lower and upper x limit:
        two floats seperated by space (default=auto)'''
    parser.add_argument('-x', '--xlimits', nargs='+', type=float, default=None,
                        metavar='xlim', help=msg)
    msg = '''lower and upper y limit:
        two floats seperated by space (default=auto)'''
    parser.add_argument('-y', '--ylimits', nargs='+', type=float, default=None,
                        metavar='ylim', help=msg)
    msg = 'command whether to print the figures as PDF [Y/N] (default="N")'
    parser.add_argument('-c', '--command', default='N',
                        metavar='COM', help=msg)
    args = parser.parse_args()

    xlim = args.xlimits
    try:
        xlim = tuple(args.xlimits)
    except TypeError:
        xlim = None
    ylim = args.ylimits
    try:
        ylim = tuple(args.ylimits)
    except TypeError:
        ylim = None

    xx, wavefuncs, energies, pot, expval = solveio._read_results(args.inputdir)
    visualizer.wavevisualizer(xx, wavefuncs, energies,
                              pot, expval, args.stretch, xlim,
                              ylim)
    if args.command == "Y":
        path = os.path.join(args.inputdir, "schrodinger_plot.pdf")
        plt.savefig(path)
    else:
        plt.show()


if __name__ == "__main__":
    main()
