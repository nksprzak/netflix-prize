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
        s = "1:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, ":")

    def test_read_2 (self) :
        s = "2488120\n"
        i, j = netflix_read(s)
        self.assertEqual(i, 2488120)
        self.assertEqual(j, "")

    def test_read_3 (self) :
        s = "1904905\n"
        i, j = netflix_read(s)
        self.assertNotEqual(i, 1904906)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval(3.49, 4.63)
        self.assertEqual(v, 4)

    def test_eval_2 (self) :
        v = netflix_eval(3.49, 4.00)
        self.assertEqual(v, 4)

    def test_eval_3 (self) :
        v = netflix_eval(4.19, 3.79)
        self.assertEqual(v, 4)

    def test_eval_4 (self) :
        v = netflix_eval(3.30, 4.38)
        self.assertEqual(v, 4)

    def test_eval_5 (self) :
        v = netflix_eval(3.30, 4.17)
        self.assertEqual(v, 4)

    def test_eval_6 (self) :
        v = netflix_eval(3.60, 3.44)
        self.assertEqual(v, 4)

    def test_eval_7 (self) :
        v = netflix_eval(2.79, 4.00)
        self.assertEqual(v, 3)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1.9)
        self.assertEqual(w.getvalue(), "1.9 \n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 2.79)
        self.assertEqual(w.getvalue(), "2.79 \n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 3.5)
        self.assertEqual(w.getvalue(), "3.5 \n")

    def test_print_4 (self) :
        w = StringIO()
        netflix_print(w, 1904905)
        self.assertEqual(w.getvalue(), "1904905 \n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), '1: \n3.7 \n3.3 \n3.6 \n4.7 \n3.7 \n3.9 \nRMSE: 0.97\n')
    
    def test_solve_2 (self) :
        r = StringIO("1000:\n2326571\n977808\n1010534\n1861759\n79755\n98259\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), '1000: \n3.2 \n2.9 \n2.6 \n4.6 \n3.7 \n3.3 \nRMSE: 0.97 \n')
    def test_solve_3 (self) :
        r = StringIO("10007:\n1204847\n2160216\n248206\n835054\n1064667\n2419805\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), '10007: \n2.0 \n2.6 \n2.2 \n2.2 \n2.0 \n2.5 \nRMSE: 0.97 \n')

# ----
# main
# ----

if __name__ == "__main__" :
    main()
