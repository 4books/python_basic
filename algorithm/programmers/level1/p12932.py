"""
https://school.programmers.co.kr/learn/courses/30/lessons/12932
자연수 뒤집어 배열로 만들기
"""


def solution(n):
    arr = list(str(n))
    arr.reverse()
    m = list(map(int, arr))
    return m


if __name__ == '__main__':
    l = solution(12345)
    print(l)
