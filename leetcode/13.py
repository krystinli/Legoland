# Solution 1
# Runtime: 55 ms, faster than 72.26%
# Memory Usage: 13.9 MB, less than 79.10%

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "A") # A means 4
        s = s.replace("IX", "B") # B means 9
        s = s.replace("XL", "E") # E means 40
        s = s.replace("XC", "F") # F means 90
        s = s.replace("CD", "G") # G means 400
        s = s.replace("CM", "H") # H means 900
        
        sum = 0
        for i in list(s):
            if i == "I":
                sum += 1
            elif i == "V":
                sum += 5
            elif i == "X":
                sum += 10
            elif i == "L":
                sum += 50
            elif i == "C":
                sum += 100
            elif i == "D":
                sum += 500
            elif i == "M":
                sum += 1000
            elif i == "M":
                sum += 1000
            elif i == "A":
                sum += 4
            elif i == "B":
                sum += 9
            elif i == "E":
                sum += 40
            elif i == "F":
                sum += 90
            elif i == "G":
                sum += 400
            elif i == "H":
                sum += 900
        return sum 
        
        
