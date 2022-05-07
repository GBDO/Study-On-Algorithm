# test_baekjoon_2675.py
def sr_rp(s):
    result = ''
    String = s
    n, String = String.split()


    for i in String:
        for _ in range(int(n)):
            result += i 
    return result
  
# 테스트코드
def test_sr_rp():
    assert sr_rp('5 /HTP') == '///HHHHHTTTTTPPPPP'
