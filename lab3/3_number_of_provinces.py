class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                while stack:
                    city = stack.pop()
                    if not visited[city]:
                        visited[city] = True
                        for j in range(n):
                            if isConnected[city][j] == 1 and not visited[j]:
                                stack.append(j)
                provinces += 1

        return provinces

