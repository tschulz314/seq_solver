#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:08:25 2020

@author: tommy
"""
import numpy as np
import scipy.linalg as la
import scipy.interpolate
import solveio


def interpolation():
    '''
    interpolates a given potential
    '''
    xs = solveio.read_input()[6][:, 0]
    pots = solveio.read_input()[6][:, 1]
    if solveio.read_input()[4] == "linear":
        pot = scipy.interpolate.interp1d(xs, pots)
    elif solveio.read_input()[4] == "cspline":
        pot = scipy.interpolate.CubicSpline(xs, pots)
    else:
        pot = scipy.interpolate.KroghInterpolator(xs, pots)
    return pot
# interpolation()


def hamiltonian():
    """
    calculates the hamiltonian
    """
    n = solveio.read_input()[2]
    xx = np.linspace(solveio.read_input()[1][0], solveio.read_input()[1][1], n)
    pot = interpolation()
    mass = solveio.read_input()[0]
    delta = (np.abs(xx[0] - xx[1])) / 2
    a = 1.0 / (mass * delta**2)
    maindiag = np.zeros(n)
    for ii in range(0, n):
        maindiag[ii] = a + pot(xx[ii])
    secdiag = (-a / 2) * np.ones(n-1)
    return maindiag, secdiag, xx, delta
hamiltonian()


def solver():
    maind = hamiltonian()[0]
    secd = hamiltonian()[1]
    neigen = (solveio.read_input()[3][0] -1, solveio.read_input()[3][1]-1)
    temp = la.eigh_tridiagonal(maind, secd, select='i', select_range=neigen)
    energies, wavefunc = temp
    x = hamiltonian()[2]
    return energies , wavefunc, x
solver()


def normalization():
    delta = hamiltonian()[3]
    wavefunc = solver()[1]
    npoints, nfunc = wavefunc.shape
    for ii in range(0, nfunc):
        psisquared = 0
        for jj in range(0, npoints):
            psisquared +=np.abs(wavefunc[:, ii][jj])**2
        psisquared *= delta
        wavefunc[:, ii] = wavefunc[:, ii] / np.sqrt(psisquared)
    return wavefunc
# normalization()


def expectedvalue():
    wavefunc = normalization()
    npoints, nfunc = wavefunc.shape
    xx = hamiltonian()[2]
    delta = hamiltonian()[3]
    expval = np.zeros((nfunc, 2), dtype="float")
    for ii in range(0, nfunc):
        for jj in range(0, npoints):
            expval[ii][0] += np.abs(wavefunc[:, ii][jj])**2 * xx[jj]
            expval[ii][1] += np.abs(wavefunc[:, ii][jj])**2 * xx[jj]**2
        expval[ii][0] *= delta
        expval[ii][1] *= delta
        expval[ii][1] = np.sqrt(np.abs(expval[ii][1]-expval[ii][0]**2))
    return expval
# expectedvalue()










