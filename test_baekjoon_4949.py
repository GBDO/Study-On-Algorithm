# -*- coding: utf-8 -*-
"""test_baekjoon_4949.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ze1qed9OKzbvNSd_TKD5k2TAFZkCpVX3
"""

def balance(inp):
    stack = [] 
    flag = 0
    for c in inp:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or '(' != stack.pop():
                flag = 1
                break
        elif c == ']':
            if len(stack) == 0 or '[' != stack.pop():
                flag = 1
                break
    if flag == 0 and len(stack) == 0:
        return 'yes '
    else:
        return 'no '


def test_balance():
    ch = [
    'So when I die (the [first] I will see in (heaven) is a score list).',
    '[ first in ] ( first out ).',
    'Half Moon tonight (At least it is better than no Moon at all].',
    'A rope may form )( a trail in a maze.',
    'Help( I[m being held prisoner in a fortune cookie factory)].',
    '([ (([( [ ] ) ( ) (( ))] )) ]).',
    ' .'
    ]
    result = ''
    for inp in ch:
        result += balance(inp)
    assert  result == 'yes yes no no no yes yes '