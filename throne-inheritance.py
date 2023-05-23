class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.king = kingName
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.king]
        ans = []
        while stack:
            val = stack.pop(0)
            if val not in self.dead:
                ans.append(val)
            stack = self.graph[val] + stack

        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()