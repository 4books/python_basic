from collections import deque


def solution(maps):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    max_r, max_c = (len(maps), len(maps[0]))
    # 튜플 (row, col, distance)
    queue = deque([(0, 0, 1)])
    while len(queue) > 0:
        row, col, d = queue.popleft()

        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]

            if nrow < 0 or nrow >= max_r or ncol < 0 or ncol >= max_c:
                continue

            if maps[nrow][ncol] == 1 or maps[nrow][ncol] > d + 1:
                maps[nrow][ncol] = d + 1
                if nrow == max_r -1 and ncol == max_c - 1:
                    return d + 1

                queue.append((nrow, ncol, d + 1))

    return -1


if __name__ == '__main__':
    i = solution(None)
    print(i)
