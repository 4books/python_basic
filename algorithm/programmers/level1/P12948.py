"""
https://school.programmers.co.kr/learn/courses/30/lessons/12948
핸드폰 번호 가르기
"""


def solution(phone_number):
    show = phone_number[-4:]

    answer = "*" * (len(phone_number) - 4)
    answer += show
    return answer


if __name__ == '__main__':
    s = solution("01033334444")
    print(s)

