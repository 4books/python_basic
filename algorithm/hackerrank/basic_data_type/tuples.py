# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
