# Solution 1
# Runtime: 68 ms, faster than 78.51% 
# Memory Usage: 13.8 MB, less than 97.06%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(int.__str__(x))[::-1] == list(int.__str__(x))
