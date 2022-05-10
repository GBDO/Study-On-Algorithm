# -*- coding: utf-8 -*-
"""test_baekjoon_11931.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j3Oo9T10ByZbPg-7e9HJJO24tuNe-Co9
"""

import sys
def sort_num(n, input):
    num = int(n)
    ls = [0] * num 
    for k ,i in zip(range(num),input):
        tn = int(i)
        ls[k] = tn
    ls.sort(reverse = True)
    return ls
def test_sort_num():
    assert sort_num(5,[1,2,3,4,5]) == [5,4,3,2,1]