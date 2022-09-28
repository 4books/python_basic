# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    _list = []
    for _ in range(N):
        action, *value = input().split()
        if action == 'print':
            print(_list)
        elif action == 'insert':
            _list.insert(int(value[0]), int(value[1]))
        elif action == 'remove':
            _list.remove(int(value[0]))
        elif action == 'append':
            _list.append(int(value[0]))
        elif action == 'sort':
            _list.sort()
        elif action == 'pop':
            _list.pop()
        elif action == 'reverse':
            _list.reverse()

