"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906
같은 숫자는 싫어
"""


def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer


if __name__ == '__main__':
    ans = solution([])
    print(ans)
    ans = solution([1, 1, 3, 3, 0, 1, 1])
    print(ans)
    ans = solution([4, 4, 4, 3, 3])
    print(ans)
