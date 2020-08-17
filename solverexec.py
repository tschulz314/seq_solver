#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:51:25 2020

@author: tommy
"""
import numpy as np
import solveio
import solver


def main(inputdir):
    interpoltype = solveio.read_input(inputdir="schroedinger_data")[4]
    xknown = solveio.read_input(inputdir="schroedinger_data")[6][:, 0]
    potknown = solveio.read_input(inputdir="schroedinger_data")[6][:, 1]
    pot = solver.interpolation(interpoltype, xknown, potknown)

    npoints = solveio.read_input(inputdir="schroedinger_data")[2]
    xx = np.linspace(solveio.read_input(inputdir="schroedinger_data")[1][0], solveio.read_input(inputdir="schroedinger_data")[1][1], npoints)
    mass = solveio.read_input(inputdir="schroedinger_data")[0]
    delta = (np.abs(xx[0] - xx[1]))
    neigen = (solveio.read_input(inputdir="schroedinger_data")[3][0] -1, solveio.read_input(inputdir="schroedinger_data")[3][1]-1)
    energies, wavefunc = solver.seqsolver(npoints, xx, pot, mass, delta, neigen)
    wavefunc = solver.normalization(wavefunc, delta)
    expval = solver.expectedvalue(wavefunc, xx, delta)
    expval

if __name__ == "__main__":
    main("schroedinger_data")