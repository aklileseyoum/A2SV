class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = rooms[0]
        visited = set()

        while queue:
            length = len(queue)

            for idx in range(length):
                room = queue.pop(0)
                if room not in visited:
                    visited.add(room)
                    queue += rooms[room]

        for num in range(1, len(rooms)):
            if num not in visited:
                return False

        return True