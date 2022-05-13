# -*- coding: utf-8 -*-
"""test_baekjoon_5800.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zEHl2RuEQZWXLnF9CL5Q-QqTDeypzEkf
"""

def scorea(num,lss):
    for i, ls in zip(range(num),lss):
        ls = ls.split()[1:]
        gapls = [0] * (len(ls)-1)
        for j in range(len(ls)):
            ls[j] = int(ls[j])
        ls.sort(reverse= True)
        for k in range(len(ls)-1):
            gapls[k] = ls[k] - ls[k+1]
        fst = int(max(ls))
        sst = max(gapls)
        lst = int(min(ls))
        return (f'Class {int(i)+1}',f'Max {fst}, Min {lst}, Largest gap {sst}')

def test_scorea():
    assert scorea(2,['5 30 25 76 23 78','6 25 50 70 99 70 90']) == ('Class 1', 'Max 78, Min 23, Largest gap 46'), ('Class 2', 'Max 99, Min 25, Largest gap 25')