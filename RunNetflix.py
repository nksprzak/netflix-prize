#!/usr/bin/env python3

import random

# ------------------------------
# projects/netflix/RunNetflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve


if __name__ == "__main__" :
    netflix_solve(sys.stdin, sys.stdout)



"""
% cat RunNetflix.in


% RunNetflix.py < RunNetflix.in > RunNetflix.out



% cat RunNetflix.out


% pydoc3 -w Netflix
# That creates the file Netflix.html
"""
