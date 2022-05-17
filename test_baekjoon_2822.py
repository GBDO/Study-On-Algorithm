# -*- coding: utf-8 -*-
"""test_baekjoon_2822.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17udr4hsMLBZLpH5uT0502zXpaqHlVTd3
"""

def score(xls):
    ls = []
    sum = 0
    result = []
    for k in range(8):
        x = xls[k]
        ls.append([x,k+1])
    ls.sort(key = lambda x : -x[0])
    for i in range(5):
        sum += ls[i][0]
        result.append(ls[i][1])
    result.sort()
    pr = ''
    for i in range(5):
        if i == 4:
            pr += str(result[i])
        else:
            pr += str(result[i]) + ' '
    return sum, pr

def test_score():
    assert score([20, 30, 50, 48, 33, 66, 0, 64]) == 261, '3 4 5 6 8'