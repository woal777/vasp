#!/usr/bin/env python
# -*-coding:utf-8 -*-

import sys
import os
from utils import readCHGCAR

__author__ = "Germain Vallverdu <germain.vallverdu@univ-pau.fr>"
__licence__ = "GPL"


def chgsplit():
    """ read command line arguments run chgsplit and write up density in CHGCAR_up and
        down density in CHGCAR_down
    """

    # command line arguments
    args = sys.argv
    nargs = len(args)
    if nargs == 1:
        chgcarName = "CHGCAR"
    elif nargs == 2:
        chgcarName = args[1]
    else:
        print("Error, usage : chgsplit.py or chgsplit.py CHGCAR")
        exit(1)

    # read up and down density if file CHGCAR exist
    if os.path.exists(chgcarName):
        rho_up_p_down, rho_up_m_down = readCHGCAR(chgcarName, full=True)
    else:
        print("Error : File '{0}' does not exist !\n".format(chgcarName))
        exit(1)

    # compute up and down densities
    Npts = len(rho_up_p_down)
    rho_up = list()
    rho_down = list()
    for i in range(Npts):
        if rho_up_m_down[i] > 0:
            rho_up.append(rho_up_m_down[i])
            rho_down.append(0)
        else:
            rho_down.append(-rho_up_m_down[i])
            rho_up.append(0)

    print("------------------------------------------------------------")
    # names of output files
    if os.path.exists("CHGCAR_up"):
        answer = ""
        while answer != "y":
            answer = raw_input(" file CHGCAR_up exists, overwrite it ? (y/n) : ")
            if answer == "n":
                exit(0)
            elif answer == "y":
                continue
            else:
                print("hit 'y' for yes or 'n' for non")

    if os.path.exists("CHGCAR_down"):
        answer = ""
        while answer != "y":
            answer = raw_input(" file CHGCAR_down exists, overwrite it ? (y/n) : ")
            if answer == "n":
                exit(0)
            elif answer == "y":
                continue
            else:
                print("hit 'y' for yes or 'n' for non")

    print(" write up density in   : CHGCAR_up")
    print(" write down density in : CHGCAR_down")
    print("------------------------------------------------------------")

    fchgcar_up = open("CHGCAR_up", "w")
    fchgcar_down = open("CHGCAR_down", "w")

    # head of CHGCAR_up and CHGCAR_down files
    fchgcar = open(chgcarName, "r")
    end = False
    while not end:
        line = fchgcar.readline()
        if line.strip() == "":
            end = True
        fchgcar_up.write(line)
        fchgcar_down.write(line)

    # direct
    line = fchgcar.readline()
    fchgcar.close()

    fchgcar_up.write(line)
    fchgcar_down.write(line)

    # write up and down densities
    i = 0
    Npts = len(rho_up)
    while i < Npts:
        line_up = line_down = ""
        for j in range(5):
            line_up += "%18.11e " % rho_up[i]
            line_down += "%18.11e " % rho_down[i]
            i += 1
            if i >= Npts:
                break
        line_up += "\n"
        line_down += "\n"
        fchgcar_up.write(line_up)
        fchgcar_down.write(line_down)

    fchgcar_up.close()
    fchgcar_down.close()


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

if __name__ == "__main__":
    chgsplit()
