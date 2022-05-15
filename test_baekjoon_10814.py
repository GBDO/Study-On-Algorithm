# -*- coding: utf-8 -*-
"""test_baekjoon_10814.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpIQ5TLm9bpYsWY2oUQ2ujAvAyv3eBlA
"""

def agesort(num, ages):
    full = []
    for k in range(num):
        full.append(f'{k} {ages[k]}')
    full.sort(key = lambda x : (int(x.split()[1]), int(x.split()[0]) ))
    result = ''
    for i in range(num):
        x = full[i].split()
        if i == (num-1):
            result += f'{x[1]} {x[2]}'
        else:
            result += f'{x[1]} {x[2]}' + ' '
    return result
def test_agesort():
    assert agesort(3, ['21 Junkyu','21 Dohyun','20 Sunyoung']) == '20 Sunyoung 21 Junkyu 21 Dohyun'