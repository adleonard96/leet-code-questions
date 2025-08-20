class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_salary = sorted(salary)

        count = len(sorted_salary) - 2
        total = 0
        for i in range(1, len(sorted_salary)-1):
            total += sorted_salary[i]

        return total / count