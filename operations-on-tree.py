class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(parent)
        self.child = { i : [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True        

    def upgrade(self, num: int, user: int) -> bool:
        number = num
        while number != -1:
            if self.locked[number]:
                return False
            number = self.parent[number]
        locked, queue = 0, deque([num])
        while queue:
            n = queue.popleft()
            if self.locked[n]:
                self.locked[n] = None
                locked += 1
            queue.extend(self.child[n])

        if locked > 0:
            self.locked[num] = user
        return locked > 0


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)