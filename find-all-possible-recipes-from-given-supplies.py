class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        length = len(recipes)

        for idx in range(length):
            indegree[recipes[idx]] = len(ingredients[idx])
            for idx2 in range(len(ingredients[idx])):
                graph[ingredients[idx][idx2]].append(recipes[idx])
                
        queue = deque(supplies)
        recipes = set(recipes)
        answer = []
        
        while queue:
            val = queue.popleft()

            if val in recipes:
                answer.append(val)

            for rec in graph[val]:
                indegree[rec] -= 1

                if indegree[rec] == 0:
                    queue.append(rec)
                    
        return answer