# -*- coding: utf-8 -*-
"""test_baekjoon_10866_try_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zIF3utdKm4axJ8yLIREKdL6WjWT-HNOp
"""

from collections import deque


def deck(rep, ls):
    result = ''
    que = deque()
    for t in ls:
        cm=list(t.split())
        if len(cm) == 2:
            cm, num = cm[0], cm[1]
        else:
            cm = cm[0]
        
        if cm == 'push_front':
            que.insert(0,num)
        elif cm == 'push_back':
            que.append(num)
        elif cm == 'pop_front':
            if len(que) == 0:
                result += '-1 '
            else:
                x = que.popleft()
                result += str(x)+' '
        elif cm == 'pop_back':
            if len(que) == 0:
                result += '-1 '
            else:
                x = que.pop()
                result += str(x)+' '
        elif cm == 'size':
            x = len(que)
            result += str(x)+' '
        elif cm == 'empty':
            if len(que) == 0:
                result += '1 '
            else:
                result += '0 '
        elif cm == 'front':
            if len(que) == 0:
                result += '-1 '
            else:
                result += str(que[0]) + ' '
        elif cm == 'back':
            if len(que) == 0:
                result += '-1 '
            else:
                result += str(que[-1])+' '
    return result
    
def test_deck():
    ls = ['push_back 1','push_front 2','front','back','size','empty','pop_front','pop_back','pop_front','size','empty','pop_back','push_front 3','empty','front']
    assert deck(15,ls) == '2 1 2 0 2 1 -1 0 1 -1 0 3 '