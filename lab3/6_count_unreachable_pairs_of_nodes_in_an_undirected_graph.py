class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        component_sizes = []

        for i in range(n):
            if not visited[i]:
                size = 0
                queue = [i]
                visited[i] = True
                while queue:
                    node = queue.pop(0)
                    size += 1
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                component_sizes.append(size)

        total_pairs = n * (n - 1) // 2

        reachable_pairs = 0
        for size in component_sizes:
            reachable_pairs += size * (size - 1) // 2

        return total_pairs - reachable_pairs

