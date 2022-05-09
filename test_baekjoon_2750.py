# -*- coding: utf-8 -*-
"""test_baekjoon_2750.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mwPe1falDK9nn5Px24qe-wcsxw-32DlY
"""

def sort_num(num, inp):
    ls = [0]*num
    for i, n in zip(range(num),inp):
        ls[i] = int(n)
        if i == 0:
            pass
    ls.sort()
    result = ''
    for i in range(len(ls)):
        result += str(ls[i])+' '
        if i == len(ls) - 1:
            result += str(ls[i])
    return result

def test_sort_num():
    assert sort_num(5, [5, 2, 3, 4, 1]) == '1 2 3 4 5'