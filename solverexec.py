#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:51:25 2020

@author: tommy
"""
import solveio
import solver


def main(inputdir="testdata/harmonic_oscillator.inp"):
    """
    Main function for solving the schroedinger equation
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
    write_output(energies, xx, wavefunc, expval, pot)


if __name__ == "__main__":
    main()
