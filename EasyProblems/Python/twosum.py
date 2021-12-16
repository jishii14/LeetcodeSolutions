class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexed_nums = dict()
        for i in range(0, len(nums)):
            match = target - nums[i]
            if match in indexed_nums.keys():
                return [indexed_nums[match], i]
            
            indexed_nums[nums[i]] = i
        return -1