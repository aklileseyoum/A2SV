class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        new_list = []
        for index in range(len(points)):
            distance = (points[index][0] ** 2) + (points[index][1] ** 2)
            new_list.append([index, distance])

        new_list.sort(key=lambda x:x[1])

        for key in new_list:
            if k > 0:
                answer.append(points[key[0]])
                k -= 1
            else:
                break

        return answer
