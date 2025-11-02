class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        group = [-1] * n

        for i in range(n):
            if group[i] == -1:
                queue = [i]
                group[i] = 0

                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if group[neighbor] == -1:
                            group[neighbor] = 1 - group[node]
                            queue.append(neighbor)
                        elif group[neighbor] == group[node]:
                            return False

        return True

