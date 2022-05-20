# -*- coding: utf-8 -*-
"""test_baekjoon_1302.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m61fvJ_FvWxdlQo4zUc81BMape2iCFbi
"""

from collections import Counter
def bestseller(ls):
    cnt = Counter(ls)
    tar = cnt.most_common()
    tar.sort(key = lambda x: (-x[1],x[0]))
    return str(tar[0][0])
def test_bestseller():
    assert bestseller(['top','top','top','top','kimtop']) == 'top'
    assert bestseller(['b','b','a','a']) == 'a'