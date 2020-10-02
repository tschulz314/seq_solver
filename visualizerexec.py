"""
Executable python script for visualizing the results of the one dimensional
schroedinger equation.
"""
import schrodinger_solver.solveio as solveio
import schrodinger_solver.visualizer as visualizer
import matplotlib.pyplot as plt
import os.path


def main(inputdir, stretch, xlim, ylim, inputpdf):
    """
    Main function for visualizing the results of the one dimensional
    schroedinger equation.
    """
    xx, wavefuncs, energies, pot, expval = solveio._read_results(inputdir)
    visualizer.wavevisualizer(xx, wavefuncs, energies,
                              pot, expval, stretch, xlim, ylim)
    if inputpdf == "Y":
        path = os.path.join(inputdir, "schrodinger_plot.pdf")
        plt.savefig(path)
    else:
        plt.show()


if __name__ == "__main__":
    inputdir = input("Enter the path to the files to plot: ")
    stretch = float(input("Enter a number to scale the wavefunctions(float, default=1): ") or 1.0)
    try:
        xlim = eval(input("Set the x limits (xmin, xmax): "))
    except SyntaxError:
        xlim = None
    try:
        ylim = eval(input("Set the y limits (ymin, ymax): "))
    except SyntaxError:
        ylim = None
    inputpdf = input("Save results as a pdf? (Y/N): ")
    main(inputdir, stretch, xlim, ylim, inputpdf)
