# -*- coding: utf-8 -*-
"""
Routines to test the solver:
"""
import numpy as np
import os.path
import pytest
import solveio
import solver

ABSOLUTE_TOLERANCE = 1e-9
RELATIVE_TOLERANCE = 1e-8

TESTNAMES = ["assymetric_well", "double_well_lin",
             "double_well_spline", "finite_well",
             "harmonic_oscillator", "infinite_well"]


def get_solver_data(inputdir):
    """
    Function
    """
    temp = solveio.read_input(inputdir)
    interpoltype = temp[3]
    xknown = temp[5][:, 0]
    potknown = temp[5][:, 1]
    pot = solver.interpolation(interpoltype, xknown, potknown)
    xinfo = temp[1]
    mass = temp[0]
    eigenrange = temp[2][0] - 1, temp[2][1] - 1
    catcher = solver.seqsolver(xinfo, pot, mass, eigenrange)
    energies, xx, wavefunc, delta = catcher
    wavefunc = solver.normalization(wavefunc, delta)
    expval = solver.expectedvalue(wavefunc, xx, delta)
    return xx, pot, expval, energies


@pytest.mark.parametrize("testname", TESTNAMES)
def test_potential(testname):
    path = os.path.join("testdata", testname)
    temp = get_solver_data(path)
    xx, pot = temp[0], temp[1]
    potential = np.zeros(xx.shape[0])
    for ii in range(0, xx.shape[0]):
        potential[ii] = pot(xx[ii])
    path = os.path.join(path, testname)
    refpotential = solveio._read_testdata(path)[0]
    assert np.allclose(refpotential, potential, atol=ABSOLUTE_TOLERANCE,
                       rtol=RELATIVE_TOLERANCE)


@pytest.mark.parametrize("testname", TESTNAMES)
def test_expvalues(testname):
    path = os.path.join("testdata", testname)
    expval = get_solver_data(path)[2]
    path = os.path.join(path, testname)
    refexpval = solveio._read_testdata(path)[1]
    assert np.allclose(refexpval, expval, atol=ABSOLUTE_TOLERANCE,
                       rtol=RELATIVE_TOLERANCE)


@pytest.mark.parametrize("testname", TESTNAMES)
def test_energy(testname):
    path = os.path.join("testdata", testname)
    energy = get_solver_data(path)[3]
    path = os.path.join(path, testname)
    refenergy = solveio._read_testdata(path)[2]
    assert np.allclose(refenergy, energy, atol=ABSOLUTE_TOLERANCE,
                       rtol=RELATIVE_TOLERANCE)
