class MyHashMap:

    def __init__(self):
        self.graph = {}

    def put(self, key: int, value: int) -> None:
        self.graph[key] = value

    def get(self, key: int) -> int:
        if key not in self.graph:
            return -1
        return self.graph[key]

    def remove(self, key: int) -> None:
        if key in self.graph:
            del self.graph[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)