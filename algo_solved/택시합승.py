import heapq
import math

def solution(n, s, a, b, fares):

    link = [[] for _ in range(n+1)]

    for x, y, z in fares:
        link[x].append([z, y])
        link[y].append([z, x])

    def dijkstra(start):
        dist = [math.inf] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    answer = math.inf

    for i in range(1, n + 1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    answer = 0
    return answer