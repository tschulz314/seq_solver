# -*- coding: utf-8 -*-
"""
Routines to test the solver:
"""
import numpy as np
import os.path
import pytest
import solveio
import solverexec


TOLERANCE = 1e-8
TESTNAMES = ["assymetric_well", "double_well_lin",
             "double_well_spline", "finite_well",
             "harmonic_oscillator", "infinite_well"]


@pytest.mark.parametrize("testname", TESTNAMES)
def test_potential(testname):
    refpotential = solveio._read_testdata(testname)[0]
    path = os.path.join(testname, ".inp")
    path = path.replace("/", "")
    path = os.path.join("testdata", path)
    temp = solverexec.main(inputdir=path, outputfiles=False)
    xx, pot = temp[0], temp[1]
    potential = np.zeros(xx.shape[0])
    for ii in range(0, xx.shape[0]):
        potential[ii] = pot(xx[ii])
    assert np.all(np.abs(refpotential - potential) < TOLERANCE)


@pytest.mark.parametrize("testname", TESTNAMES)
def test_expvalues(testname):
    refexpval = solveio._read_testdata(testname)[1]
    path = os.path.join(testname, ".inp")
    path = path.replace("/", "")
    path = os.path.join("testdata", path)
    expval = solverexec.main(inputdir=path, outputfiles=False)[2]
    assert np.all(np.abs(refexpval - expval) < TOLERANCE)
