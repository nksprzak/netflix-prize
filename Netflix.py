#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import numpy
import json
import requests
import os
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

def netflix_eval(movie_offset, user_offset):
    """
    ....
    """
    return round(3.7 + (float(movie_offset) - 3.7) + (float(movie_offset) - 3.7), 1)


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
    w.write(str(i).strip("\n") + "\n")

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
#    w.write("{")
#    index = 0
#    with open('/u/downing/cs/netflix/movie_titles.txt', encoding = "ISO-8859-1") as data_file:
#        for line in data_file:
#            movie = line.split(",")[0]
#            #print(movie)
#            year = line.split(",")[1]
#            w.write("\"" + movie + "\"" + ": " + year)
#            if index != 17770:
#                w.write(", ")
#            index += 1
#    w.write("}")



    # with open('/u/ebanner/netflix-tests/ldy224-movie_avg_score.json') as data_file:
    #     movie_ave_score = json.load(data_file)

    # w.write("{")
    # customer_map = {}
    # for i in range(1, 17771):
    #     istr = str(i)
    #     zeros = "0" * (5 - len(istr))
    #     path = '/u/downing/cs/netflix/training_set/mv_00' + zeros + istr + '.txt'
    #     index = 0
    #     with open(path) as data_file:
    #         movie_id = 0
    #         for line in data_file:
    #             if index == 0:
    #                 movie_id = line[:-2]
    #             if index != 0:
    #                 i = line.split(",")[0]
    #                 j = line.split(",")[1]
    #                 if str(i) in customer_map:
    #                     count = customer_map[str(i)]["count"]
    #                     customer_map[str(i)]["count"] += 1
    #                     ave_by_movie = customer_map[str(i)]["ave_by_movie"]
    #                     print("old_ave: " + str(ave_by_movie))
    #                     customer_map[str(i)]["ave_by_movie"] = (ave_by_movie * count + (int(j) - movie_ave_score[str(movie_id)])) / (count + 1)
    #                     print("new_ave: " + str((ave_by_movie * count + (int(j) - movie_ave_score[str(movie_id)])) / (count + 1)))
    #                 else: 
    #                     customer_map[str(i)] = {"count": 1, "ave_by_movie": (int(j) - movie_ave_score[str(movie_id)])}
    #                     # customer_map[str(i)]["ave_by_movie"] = (j - movie_ave_score[str(i)])
    #             index += 1
                
    # map_len = len(customer_map)
    # index = 0
    # for i in customer_map:
    #     w.write("\"" + str(i) + "\"" + ":" + "{")
    #     w.write("\"count\" :" + str(customer_map[str(i)]["count"]) + ", " + "\"ave_by_movie\": " + str(customer_map[str(i)]["ave_by_movie"]))
    #     w.write("}")
    #     if index != map_len - 1:
    #         w.write(", ")
    #     index += 1
    # w.write("}")


    # w.write("{")
    # movie_map = {}
    # for i in range(1, 17771):
    #     istr = str(i)
    #     zeros = "0" * (5 - len(istr))
    #     path = '/u/downing/cs/netflix/training_set/mv_00' + zeros + istr + '.txt'
    #     index = 0
    #     with open(path) as data_file:
    #         numlines = sum(1 for line in data_file) - 1
    #         # print(path)
    #         # print(numlines)
    #         movie_map[str(i)] = numlines

    # index = 0
    # for i in movie_map:
    #     w.write("\"" + str(i) + "\" :" + str(movie_map[str(i)]))
    #     if index != len(movie_map) - 1:
    #         w.write(", ")
    #     index += 1

    # w.write("}") 


    if os.path.isfile('/u/ebanner/netflix-tests/scm2454-movie_cache'):
        with open('/u/ebanner/netflix-tests/scm2454-movie_cache') as data_file:
            movie_ave_score = json.load(data_file)
    else:
        response = requests.get('http://www.cs.utexas.edu/users/ebanner/netflix-tests/scm2454-movie_cache')
        movie_ave_score = response.json()


    if os.path.isfile('/u/ebanner/netflix-tests/scm2454-user_cache'):
        with open('/u/ebanner/netflix-tests/scm2454-user_cache') as data_file:
            cust_ave_score = json.load(data_file)

    else:
        response_1 = requests.get('http://www.cs.utexas.edu/users/ebanner/netflix-tests/sscm2454-user_cache')
        cust_ave_score = response_1.json()

    
    # with open('UserContent.json') as data_file:
    #     cust_rating_count = json.load(data_file)

    # with open('movie_rating_count.json') as data_file:
    #     movie_rating_count = json.load(data_file)


    total_ratings = 0
    total_users = 0
    total_max = 0

    # for i in cust_rating_count:
    #     cur_count = int(cust_rating_count[str(i)]["count"])
    #     total_users += 1;
    #     total_ratings += cur_count
    #     if (cur_count) > total_max:
    #         total_max = cur_count
    # total_rating_count_ave = total_ratings // total_users

    # for i in cust_rating_count:
    #     cur_count = int(cust_rating_count[str(i)]["count"])
    #     # cur_ave = float(cust_rating_count[str(i)]["ave_by_movie"])
    #     # print("count " + str(cur_count))
    #     # print("ave " + str(cur_ave))
    #     total_users += 1;
    #     total_ratings += cur_count
    #     if (cur_count) > total_max:
    #         total_max = cur_count
    # total_rating_count_ave = total_ratings // total_users
    # print("total_ratings" + str(total_ratings))
    # print("total_users" + str(total_users))
    # print("total max" + str(total_max))
    # print("total rating count ave" + str(total_rating_count_ave))

    current_movie = -1
    index = 20
    for num in r:
        i, j = netflix_read(num)
        i = int(i)
        if j == ':':
            netflix_print(w, num)
            current_movie = i
        else:

            # print("movie: " + str(movie_ave_score[str(current_movie)]))
            # print("cust: " + str(cust_ave_score[str(i)]))
            v = netflix_eval(movie_ave_score[str(current_movie)], cust_ave_score[str(i)])
            # print("v: " + str(v))
            # current_movie_rating_count = movie_rating_count[str(current_movie)]
            # movie_skew = 1
            # if current_movie_rating_count > 50000:
            #     movie_skew *= 1.1
            # else: 
            #     if current_movie_rating_count > 20000:
            #         movie_skew *= 1.2
            #     else:
            #         if current_movie_rating_count > 5000:
            #             movie_skew *= 1.4
            #         else:
            #             movie_skew *= 1.6
            # if abs(int(cust_rating_count[str(i)]["count"]) - total_rating_count_ave) > 7000:
            #     user_skew = ((.5 * abs(.5 - abs(int(cust_rating_count[str(i)]["count"]) - total_rating_count_ave) // (total_max - total_rating_count_ave)))) // 2
            #     v = round(3.7 + (user_skew * float(movie_ave_score[str(current_movie)]) - 3.7) + ((1- user_skew) * float(cust_ave_score[str(i)]) - 3.7), 2)
            # else:
            v = round(3.7 + (float(movie_ave_score[str(current_movie)]) - 3.7) + (float(cust_ave_score[str(i)]) - 3.7), 2)
            # if v > 5:
            #     v = 5          
            # if abs(int(cust_rating_count[str(i)]["count"]) - total_rating_count_ave) > 40000:
            #     user_skew = ((.5 * abs(.5 - abs(int(cust_rating_count[str(i)]["count"]) - total_rating_count_ave) // (total_max - total_rating_count_ave))))* 2
            #     v = netflix_eval(movie_skew * user_skew * movie_ave_score[str(current_movie)] + cust_rating_count[str(i)]["ave_by_movie"], (2 - movie_skew) * (2 - user_skew) * cust_ave_score[str(i)])
            # else:          
            #     v = netflix_eval(movie_skew * movie_ave_score[str(current_movie)] + cust_rating_count[str(i)]["ave_by_movie"], (2 - movie_skew) * cust_ave_score[str(i)])
            # final = netflix_eval(.5*(3.228), 1.5*(v))
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
            x = float(x.strip())
            y = int(y.strip())
            actArr.append(x)
            estArr.append(y)

    res = netflix_get_rsme(actArr, estArr)
    netflix_print(w, res)       
