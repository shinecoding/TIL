class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        pre = 0
        
        for n in s:
            cur = numerals[n]
            if cur > pre:
                sum -= pre*2
            pre = cur
            sum += cur
            
       
        return sum