#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import numpy
import json
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


# def netflix_read_2(s):
#     """
#     read two ints
#     s a string
#     return a list of two ints, representing the beginning and end of a range, [i, j]
#     """
#     if ':' in s:
#         a = s.strip(' \n')
#         num = int(a.strip(':'))
#         val = [num, ':']
#         return val
#     else:
#         return s.strip('\n')


def netflix_solve(r, w):
    """
    r a reader
    w a writer
    """

    # w.write("{")
    # customer_map = {}
    # for i in range(1, 17771):
    #     istr = str(i)
    #     zeros = "0" * (5 - len(istr))
    #     path = '/u/downing/cs/netflix/training_set/mv_00' + zeros + istr + '.txt'
    #     index = 0
    #     with open(path) as data_file:
    #         for line in data_file:
    #             if index != 0:
    #                 i = line.split(",")[0]
    #                 if str(i) in customer_map:
    #                     customer_map[str(i)] += 1
    #                 else: 
    #                     customer_map[str(i)] = 1
    #             index += 1
                
    # map_len = len(customer_map)
    # index = 0
    # for i in customer_map:
    #     w.write("\"" + str(i) + "\"" + ":")
    #     w.write(str(customer_map[str(i)]))
    #     if index != map_len - 1:
    #         w.write(", ")
    #     index += 1
    # w.write("}")




    with open('/u/ebanner/netflix-tests/ldy224-movie_avg_score.json') as data_file:
        movie_ave_score = json.load(data_file)

    with open('/u/ebanner/netflix-tests/crb3385-user_ratings_avg.json') as data_file:
        cust_ave_score = json.load(data_file)
    
    with open('UserVoteCount.json') as data_file:
        cust_rating_count = json.load(data_file)

    total_ratings = 0
    total_users = 0
    total_max = 0
    for i in cust_rating_count:
        cur_count = int(cust_rating_count[str(i)])
        total_users += 1;
        total_ratings += cur_count
        if (cur_count) > total_max:
            total_max = cur_count
    total_rating_count_ave = total_ratings // total_users
    # print("total_ratings" + str(total_ratings))
    # print("total_users" + str(total_users))
    # print("total max" + str(total_max))
    # print("total rating count ave" + str(total_rating_count_ave))
    current_movie = -1
    index = 20
    for num in r:
        i, j = netflix_read(num)
        if j == ':':
            #w.write("current_movie:" + str(current_movie) + "\n")
            netflix_print(w, num)
            current_movie = i
        else:
            #w.write("current_movie:" + str(current_movie) + "\n")
            #w.write("customer:" + str(i) + "\n")
            #w.write("   movie score:" + str(movie_ave_score[str(current_movie)]) + "\n")
            if abs(int(cust_rating_count[str(i)]) - total_rating_count_ave) > 13000:
                # print("going by user skew")
                user_skew = (.5 * abs(.5 - abs(int(cust_rating_count[str(i)]) - total_rating_count_ave) // (total_max - total_rating_count_ave))) // 2
                # print("" + str(user_skew) )
                v = netflix_eval(user_skew * movie_ave_score[str(current_movie)], (1 - user_skew) *cust_ave_score[str(i)])
            else:
                # print("Not going by user skew")
                v = netflix_eval(movie_ave_score[str(current_movie)], cust_ave_score[str(i)])
            #w.write("   est_review:" + str(v) + "\n")
            netflix_print(w, v)
        # remove this stuff later
        # index -= 1
        # if index == 0:
        #    break
    actArr = []
    estArr = []
    with open("RunNetflix.out") as textfile1, open("probe_actual.txt") as textfile2: 
        for x, y in zip(textfile1, textfile2):
            i, j = netflix_read(x)
            if (j == ':'):
                continue
            x = int(x.strip())
            y = int(y.strip())
            actArr.append(x)
            estArr.append(y)

    res = netflix_get_rsme(actArr, estArr)
    netflix_print(w, res)       
