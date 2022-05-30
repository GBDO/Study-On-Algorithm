# -*- coding: utf-8 -*-
"""test_baekjoon_10828_try_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17B_apCC6z8Y6Au4U_kU-06VEQWT51onl
"""

def stackf(stack,input):
    comend = ''
    inp = 0
    x = list(input.split())
    if len(x) == 2:
        comend, inp = x
    else:
        comend = x[0]
    if comend == 'push':
        stack.append(inp)
    elif comend == 'pop':
        if len(stack) == 0:
            return -1
        else:
            return stack.pop()
    elif comend == 'size':
        return len(stack)
    elif comend == 'empty':
        if len(stack) == 0:
            return 1
        else:
            return 0
    elif comend == 'top':
        if len(stack) > 0:
            return stack[-1]
        else:
            return -1

def test_stack():
    stack = []
    result = []
    ls = ['push 1','push 2','top','size','empty','pop','pop','pop','size','empty','pop','push 3','empty','top']
    for k in ls:
        result.append(stackf(k))
    assert result == [2,2,0,2,1,-1,0,1,-1,0,3]