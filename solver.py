#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:08:25 2020

@author: tommy
"""
import numpy as np
import solveio
import scipy.linalg as la
import scipy.interpolate
# import matplotlib.pyplot as plt


def interpolation():
    xs = solveio.read_input()[6][:, 0]
    pots = solveio.read_input()[6][:, 1]
    if solveio.read_input()[4] == "linear":
        #print("lin")
        pot = scipy.interpolate.interp1d(xs, pots)
    elif solveio.read_input()[4] == "cspline":
        #print("spline")
        pot = scipy.interpolate.CubicSpline(xs, pots)
    elif solveio.read_input()[4] == "polynomial":
        #print("pol")
        pot = scipy.interpolate.KroghInterpolator(xs, pots)

    return pot
# interpolation()


def hamiltonian():
    n = solveio.read_input()[2]
    x = np.linspace(solveio.read_input()[1][0], solveio.read_input()[1][1], n)
    pot = interpolation()
    m = solveio.read_input()[0]
    delta = (abs(x[0] - x[1])) / 2
    a = 1.0 / (m * delta)

    maindiag = np.ones(n)
    for ii in range(0, n):
        maindiag[ii] = a + pot(x[ii])
    secdiag = (-a / 2) * np.ones(n-1)
    return maindiag, secdiag, x
# hamiltonian()


def solver():
    maind = hamiltonian()[0]
    secd = hamiltonian()[1]
    neigen = (read_input()[3][0]-1, read_input()[3][1]-1)
    temp = la.eigh_tridiagonal(maind, secd, select='i', select_range=neigen)
    energies, wavefunc = temp
    x = hamiltonian()[2]
    return energies, wavefunc, x, delta
solver()


def normalization():
    delta = solver()[3]
    wavefunc = solver()[1]
    npoints, nfunc = wavefunc.shape
    for ii in range(0, nfunc):
        psisquared = 0
        for jj in range(0, npoints):
            psisquared += wavefunc[:, ii][jj]
        wavefunc[:, ii] / np.sqrt(psisquared)
    return wavefunc

normalization()

def expectedvalue():
    return



# plt.plot(solver()[2], solver()[1][:, 3])
# plt.show()








