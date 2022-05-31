# -*- coding: utf-8 -*-
"""test_baekjoon_10773.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qq-4Tm8xpF3gp1uyYEbwq4h5u237S9NX
"""

# try 1
# def zero(rep, ls, inps):
#     for inp in inps:
#         if inp == 0:
#             if len(ls) != 0:
#                 x = ls.pop()
#                 sum -= x
#         else:
#             ls.append(inp)
#             sum += inp

# def test_zero():
#     ls = []
#     sum = 0
#     zero(4, ls, [3, 0, 4, 0])
#     assert sum == 0

"""UnboundLocalError: local variable 'sum' referenced before assignment

전역 변수를 함수에 입력하지 않아 인식하지 못하여 오류가 발생
"""

def zero(rep, ls, inps, sum):
    for inp in inps:
        if inp == 0:
            if len(ls) != 0:
                x = ls.pop()
                sum -= x
        else:
            ls.append(inp)
            sum += inp

def test_zero():
    ls = []
    sum = 0
    zero(4, ls, [3, 0, 4, 0], sum)
    assert sum == 0