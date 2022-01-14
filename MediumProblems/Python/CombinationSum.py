class Solution(object):
    def backtracking(self, solution, partial, sortednums, target, cur):
        if (target == 0):
            solution.append(list(partial))
            return
        
        for i in range(cur, len(sortednums)):
            if (target - sortednums[i] >= 0):
                partial.append(sortednums[i])
                self.backtracking(solution, partial, sortednums, target - sortednums[i], i)
                partial.remove(sortednums[i])
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution = []
        partial = []
        
        sortednums = sorted(list(set(candidates)))
        self.backtracking(solution, partial, sortednums, target, 0)
        
        return solution