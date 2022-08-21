# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # *args: don't know how many
        name, *line = input().split()
        # map(funtion, iterator)
        # must list or set convert
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    _list = student_marks[query_name]
    _sum = 0
    for i in range(len(_list)):
        _sum += float(_list[i])

    # f string print .2f
    # auto round. example: 56.00
    print(f'{_sum / len(_list):.2f}')
