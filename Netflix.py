#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import numpy
import json

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

def netflix_eval(movie_ave, cust_ave):
    """
    ....
    """
    # todo: include skew
    return numpy.mean([movie_ave, cust_ave])


# ----------------
# netflix_get_rsme
# ----------------

def netflix_get_rsme(expected, actual):
    """
    ....
    """
    rmse = numpy.sqrt(numpy.mean(numpy.square(expected - actual)))

    return rmse

# -------------
# netflix_print
# -------------

def netflix_print(w, i):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve(r, w):
    """
    r a reader
    w a writer
    """
    with open('/u/ebanner/netflix-tests/ldy224-movie_avg_score.json') as data_file:
        movie_ave_score = json.load(data_file)

    with open('/u/ebanner/netflix-tests/crb3385-user_ratings_avg.json') as data_file:
        cust_ave_score = json.load(data_file)
    w.write("movie score len: " + str(len(movie_ave_score)) + "\n")
    w.write("cust score len: " + str(len(cust_ave_score)) + "\n")
    w.write("movie #1 score:" + str(movie_ave_score["1"]) + "\n")
    current_movie = -1
    index = 10
    for num in r:
        i, j = netflix_read(num)
        if j == ':':
            w.write("current_movie:" + str(current_movie) + "\n")
            #netflix_print(w, num)
            current_movie = i
        else:
            #w.write("current_movie:" + str(current_movie) + "\n")
            w.write("customer:" + str(i) + "\n")
            w.write("   movie score:" + str(movie_ave_score[str(current_movie)]) + "\n")
            v = netflix_eval(movie_ave_score[str(current_movie)], cust_ave_score[str(i)])
            w.write("   est_review:" + str(v) + "\n")
            #netflix_print(w, v)
        # remove this stuff later
        index -= 1
        if index == 0:
            break
