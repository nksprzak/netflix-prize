#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import sys

# ------------
# netflix_read
# ------------

def netflix_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    if ':' in s:
        a = s.strip(' \n')
        num = int(a.strip(':'))
        val = [num, ':']
        return val
    else:
        return [int(s.strip('\n')), '']

# ------------
# netflix_eval
# ------------

def netflix_eval(first, second):
    """
    ....
    """

    return -1

# -------------
# netflix_print
# -------------

def netflix_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve(r, w):
    """
    r a reader
    w a writer
    """
    current_movie = -1
    current_movie_dict = {-1: []}
    for movie in r:
        i, j = netflix_read(movie)
        if j == ':':
            # if not current_movie == -1:
                # do something to associate gathered data with current movie
                # netflix_eval(current_movie)
            current_movie = i
            current_movie_dict = {i: []}
        else:
            current_movie_dict[current_movie].append(i)
                # todo: write some other logic for this .... maybe store the average.
                # v = netflix_eval(i, j)
                # netflix_print(w, i, j, v)