# -*- coding: utf-8 -*-
"""test_baekjoon_11652.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GyX3E6lVglUTXHM5cTqcjz-OhjEb84BU
"""

import sys
def cardch(num,cards):
    ls = []
    dic = {}
    for i in range(num):
        x = str(cards[i])
        ls.append(x)
        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    keys = list(set(ls))
    max = 0
    dap = 0
    for k in keys:
        if max < dic[k]:
            max = dic[k]
            dap = int(k)
        elif max == dic[k]:
            if dap < int(k):
                pass
            elif dap > int(k):
                dap = int(k)
        else:
            pass
    return(dap)
    
def test_cardch():
    assert cardch(5,[1,2,1,2,1]) == 1