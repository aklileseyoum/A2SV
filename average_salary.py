class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = min(salary)
        maximum = max(salary)
        salary.remove(minimum)
        salary.remove(maximum)
        summ =0
        for i in salary:
            summ += i

        average = summ / len(salary)
        return average
