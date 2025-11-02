class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        stack = [0]

        while stack:
            room = stack.pop()
            if not visited[room]:
                visited[room] = True
                for key in rooms[room]:
                    if not visited[key]:
                        stack.append(key)

        return all(visited)

