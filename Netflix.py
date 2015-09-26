#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import numpy
import json
import os
import requests
#import zip

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
        num = float(a.strip(':'))
        val = [num, ':']
        return val
    else:
        return [float(s.strip('\n')), '']

# ------------
# netflix_eval
# ------------

def netflix_eval(movie_ave, cust_ave):
    """
    ....
    """
    # todo: include skew
    return int(round(numpy.mean([movie_ave, cust_ave])))


# ----------------
# netflix_get_rsme
# ----------------

def netflix_get_rsme(actual, expected):
    """
    ....
    """
    rmse = numpy.sqrt(numpy.mean(numpy.square(numpy.subtract(actual, expected))))

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
    w.write(str(i).strip("\n") + " " + "\n")

# -------------
# netflix_solve
# -------------



def netflix_solve(r, w):
    """
    r a reader
    w a writer
    """


    if os.path.isfile('/u/ebanner/netflix-tests/scm2454-movie_cache'):
        with open('/u/ebanner/netflix-tests/scm2454-movie_cache') as data_file:
            movie_ave_score = json.load(data_file)
    else:
        response = requests.get("http://www.cs.utexas.edu/users/ebanner/netflix-tests/scm2454-movie_cache")
        movie_ave_score = response.json()


    if os.path.isfile('/u/ebanner/netflix-tests/scm2454-user_cache'):
        with open('/u/ebanner/netflix-tests/scm2454-user_cache') as data_file:
            cust_ave_score = json.load(data_file)
    else:
        response = requests.get("http://www.cs.utexas.edu/users/ebanner/netflix-tests/scm2454-user_cache")
        cust_ave_score = response.json()
    
    current_movie = -1
    index = 20
    for num in r:
        i, j = netflix_read(num)
        i = int(i)
        if j == ':':
            netflix_print(w, num)
            current_movie = i
        else:
         
            v = round(3.7 + (float(movie_ave_score[str(current_movie)]) - 3.7) + (float(cust_ave_score[str(i)]) - 3.7), 1)
         
            netflix_print(w, v)
       
    actArr = []
    estArr = []
    with open("RunNetflix.out") as textfile1, open("probe_actual.txt") as textfile2: 
        for x, y in zip(textfile1, textfile2):
            i, j = netflix_read(x)
            if (j == ':'):
                continue
            x = float(x.strip())
            y = int(y.strip())
            actArr.append(x)
            estArr.append(y)

    res = round(netflix_get_rsme(actArr, estArr), 2)
    w.write("RMSE: "+res)     
