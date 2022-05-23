# -*- coding: utf-8 -*-
"""test_baekjoon_10816_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oHMlH9pjWziwqI1YG-VuPZ3MPzfJyr_B
"""

def numcard(inp, tar):
    result = ''
    arr1 = list(map(int, inp.split()))

    dict1 = {}
    for i in arr1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    arr2 = list(map(int, tar.split()))
    for i in arr2:
        if i in dict1:
            if arr2[-1] == i:
                result += str(dict1[i])
            else:
                result += str(dict1[i]) + " "
        else:
            if arr2[-1] == i:
                result += '0'
            else:
                result += "0 "
    return result

def test_numcard():
    assert numcard('6 3 2 10 10 10 -10 -10 7 3','10 9 -5 2 3 4 5 -10') == '3 0 0 1 2 0 0 2'