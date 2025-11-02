class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            total_cost += min_dist[u]
            visited[u] = True

            for v in range(n):
                if not visited[v]:
                    xi, yi = points[u]
                    xj, yj = points[v]
                    dist = abs(xi - xj) + abs(yi - yj)
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return total_cost

