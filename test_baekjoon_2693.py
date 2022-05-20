# -*- coding: utf-8 -*-
"""test_baekjoon_2693.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQZn6ezgE2cREqijZfaT2Im63-LmWzmK
"""

import heapq
def nthlarge(num, lss):
    result = ''
    for k in range(num):
        heap = []
        ls = list(map(int, lss[k].split()))
        for i in ls:
            if len(heap) < 3:
                heapq.heappush(heap,i)
            elif heap[0]<i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        if  k == (num-1):
            result += result + str(heap[0])
        else:
            result += result + str(heap[0]) + ' '
    return result

def test_nthlarge():
    assert nthlarge(4,['1 2 3 4 5 6 7 8 9 1000','338 304 619 95 343 496 489 116 98 127','931 240 986 894 826 640 965 833 136 138','940 955 364 188 133 254 501 122 768 408']) == '8 489 931 768'