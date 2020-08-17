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
    interpoltype = solveio.read_input(inputdir="schroedinger_data")[3]
    xknown = solveio.read_input(inputdir="schroedinger_data")[5][:, 0]
    potknown = solveio.read_input(inputdir="schroedinger_data")[5][:, 1]
    pot = solver.interpolation(interpoltype, xknown, potknown)
    xinfo = solveio.read_input(inputdir="schroedinger_data")[1]
    npoints = int(xinfo[2])
    xx = np.linspace(xinfo[0], xinfo[1], npoints)
    mass = solveio.read_input(inputdir="schroedinger_data")[0]
    delta = abs(xx[0] - xx[1])
    temp = solveio.read_input(inputdir="schroedinger_data")[2]
    neigen = (temp[0] - 1, temp[1] - 1)
    energies, wavefunc = solver.seqsolver(npoints, xx, pot, mass, delta, neigen)
    wavefunc = solver.normalization(wavefunc, delta)
    expval = solver.expectedvalue(wavefunc, xx, delta)
    expval

if __name__ == "__main__":
    main("schroedinger_data")