# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    stduent = []
    # get list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stduent.append([name, score])

    # find bottom score and index
    _min = 99999
    _bottom = 99999
    for i in range(len(stduent)):
        if stduent[i][1] < _min:
            _min = stduent[i][1]
            _bottom = i

    # find runner
    _second = 99999
    for i in range(len(stduent)):
        if i == _bottom or stduent[i][1] == _min:
            continue
        if stduent[i][1] < _second:
            _second = stduent[i][1]

    # runner list
    runner = []
    for i in range(len(stduent)):
        if stduent[i][1] == _second:
            runner.append(stduent[i][0])
    runner.sort()

    # print
    answer = ""
    for i in range(len(runner)):
        answer += runner[i] + "\n"

    print(answer)
