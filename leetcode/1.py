# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9 => Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Solution 1
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                lst = [i, j]
    return lst
