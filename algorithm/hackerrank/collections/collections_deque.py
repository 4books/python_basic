# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

if __name__ == '__main__':
    q = deque()
    N = int(input())
    for i in range(N):
        _input = sys.stdin.readline().split()
        if _input[0] == 'append':
            q.append(_input[1])
        elif _input[0] == 'pop':
            q.pop()
        elif _input[0] == 'appendleft':
            q.appendleft(_input[1])
        elif _input[0] == 'popleft':
            q.popleft()

    # sys.stdout write console
    sys.stdout.write(' '.join(q))
