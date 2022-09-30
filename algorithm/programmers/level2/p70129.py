"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
이진 변환 반복
"""


def solution(s: str) -> list:
    count = 0
    zero = 0

    while True:
        if s == '1':
            break
        zero += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:] # 2진수로 바꾼다
        count += 1

    answer = [count, zero]

    return answer


print(solution("110010101001"))
