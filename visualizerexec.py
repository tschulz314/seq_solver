"""
Executable python script for visualizing the results of the one dimensional
schroedinger equation.
"""
import solveio
import visualizer
import matplotlib.pyplot as plt


def main(maindir, stretch, xlim, ylim, inputpdf):
    """
    Main function for visualizing the results of the one dimensional
    schroedinger equation.
    """
    xx, wavefuncs, energies, pot, expval = solveio._read_results(maindir)
    visualizer.wavevisualizer(xx, wavefuncs, energies, pot, expval, stretch, xlim, ylim)
    if inputpdf == "Y":
        plt.savefig("figurename.pdf")
    else:
        plt.show()


if __name__ == "__main__":
    #maindir = input("Enter the path to your main project directory: ")
    #stretch = float(input("Enter an integer for scaling the visualizations: "))
    #xlim = input("Enter your preferred limits for the x-axis: ")
    #ylim = input("..and your preferred limits for the y-axis: ")
    #inputpdf = input("Do you want do save your results as a pdf? (Y/N): ")
    maindir = "testdir/"
    stretch = 0.3
    xlim = -5, 5
    ylim = -0.1, 2.5
    inputpdf = "N"
    main(maindir, stretch, xlim, ylim, inputpdf)
