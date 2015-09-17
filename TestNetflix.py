#!/usr/bin/env python3

# -------------------------------
# projects/netflix/TestNetflix.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ----
    # read
    # ----

    def test_read_1 (self) :
        s = "1 10\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s = "999999 999999\n"
        i, j = netflix_read(s)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 999999)

    def test_read_3 (self) :
        s = "1 2\n"
        i, j = netflix_read(s)
        self.assertNotEquals(i, 2)
        self.assertNotEquals(j, 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = netflix_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = netflix_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = netflix_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = netflix_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_6 (self) :
        v = netflix_eval(50, 1)
        self.assertEqual(v, 112)

    def test_eval_7 (self) :
        v = netflix_eval(100000, 200000)
        self.assertEqual(v, 383)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 5259, 1674, 238)
        self.assertEqual(w.getvalue(), "5259 1674 238\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 97376, 91249, 333)
        self.assertEqual(w.getvalue(), "97376 91249 333\n")

    def test_print_4 (self) :
        w = StringIO()
        netflix_print(w, 985934, 982492, 427)
        self.assertEqual(w.getvalue(), "985934 982492 427\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("13954 365154\n813482 915698\n190893 442183\n153758 392830\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "13954 365154 443\n813482 915698 525\n190893 442183 449\n153758 392830 443\n")

    def test_solve_3 (self) :
        r = StringIO("1 2\n2 1\n1 4\n4 1\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n2 1 2\n1 4 8\n4 1 8\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()