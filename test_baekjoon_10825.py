# -*- coding: utf-8 -*-
"""test_baekjoon_10825.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hxn_hfZTfYGnkp1LnwCRXLrwucwZpBVz
"""

def scoresort(num, scores):
    ls = []
    result = []
    for i in range(num):
        [name, kor, eng, math]= map(str, scores[i].split())
        ls.append([name, int(kor), int(eng), int(math)])
    ls.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))
    for i in range(num):
        result.append(ls[i][0])
    return result

def test_scoresort():
   assert scoresort(12, ['Junkyu 50 60 100','Sangkeun 80 60 50','Sunyoung 80 70 100','Soong 50 60 90','Haebin 50 60 100','Kangsoo 60 80 100','Donghyuk 80 60 100','Sei 70 70 70','Wonseob 70 70 90','Sanghyun 70 70 80','nsj 80 80 80','Taewhan 50 60 90']) == ['Donghyuk','Sangkeun','Sunyoung','nsj','Wonseob','Sanghyun','Sei','Kangsoo','Haebin','Junkyu','Soong','Taewhan']