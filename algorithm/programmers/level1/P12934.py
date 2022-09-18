"""
https://school.programmers.co.kr/learn/courses/30/lessons/12934?language=python3
정수 제곱근 판별
"""
import math


def solution(n):
    num = math.sqrt(n)
    if float(num).is_integer():
        return (num + 1) ** 2
    return -1


if __name__ == '__main__':
    a = solution(121)
    print(a)
