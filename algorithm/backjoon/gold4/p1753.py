import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

# 정점 수와 간선 수
V, E = map(int, input().split())
# 시작점
K = int(input())

# dp 테이블
dp = [INF] * (V + 1)

# min Heap 초기화
heap = []

# 그래프 배열
graph = [[] for _ in range(V + 1)]


def Dijsktra(start):
    # 도착점은 0
    dp[start] = 0

    # min heap에 (가중치, 도착점) 튜플을 push 한다
    heapq.heappush(heap, (0, start))

    while heap:
        now_weight, now_node = heapq.heappop(heap)

        # 현재 dp 보다 크면 무시
        if dp[now_node] < now_weight:
            continue

        for next_weight, next_node in graph[now_node]:
            # 현재 정점에서 다음 정점까지의 거리를 새로 계산
            new_weight = next_weight + now_weight
            # 1->2가 10이고 1->3->2가 9이면 weight를 바꿈
            if new_weight < dp[next_node]:
                dp[next_node] = new_weight
                heapq.heappush(heap, (new_weight, next_node))


# 그래프 입력 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

Dijsktra(K)

for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])
