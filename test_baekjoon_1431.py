# -*- coding: utf-8 -*-
"""test_baekjoon_1431.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r62mL4qOhCpY_7bhVmzx_IY9hEQbP3bc
"""

def serialnum(num, lss):

    lss.sort(key = lambda x : (len(x), sum(int(a) for a in x if a.isdigit()), x))

    result = ''
    for g in lss:
        if g == lss[-1]:
            result += g
        else:
            result += g + ' '
    return result
def test_serialnum():
    assert serialnum(5, ['ABCD','145C','A','A910','Z321']) == 'A ABCD Z321 145C A910'