"""
https://school.programmers.co.kr/learn/courses/30/lessons/12937
짝수와 홀수
"""


def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == '__main__':
    s = solution(3)
    print(s)
