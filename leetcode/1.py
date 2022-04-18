# solution 1
# Runtime: 4287 ms, faster than 22.47% 
# Memory Usage: 14.9 MB, less than 95.81% 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    lst = [i, j]
        return lst
