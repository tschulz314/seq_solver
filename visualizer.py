#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:50:59 2020

@author: tommy
"""

import numpy as np
import matplotlib.pyplot as plt
import solveio
import solver

def wavevisualizer(stretch = 1):
    xx = solver.solver()[2]
    wavefunc = solver.normalization()
    energies = solver.solver()[0]
    pot = solver.interpolation()
    npoints, nfunc = wavefunc.shape
    for ii in range (0, nfunc):
        plt.plot(xx, stretch * solver.normalization()[:, ii] + energies[ii])
        plt.hlines(energies[ii], xx[0], xx[npoints - 1])
    plt.xlabel("x [Bohr]")
    plt.ylabel("Energy [Hartree]")
    plt.title("Potential, eigenstates, x")
    plt.show()
    return
wavevisualizer(2)