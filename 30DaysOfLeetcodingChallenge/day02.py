"""
Happy Number 
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
- Starting with any positive integer, 
- replace the number by the sum of the squares of its digits, 
- and repeat the process until the number equals 1 (where it will stay), 
- or it loops endlessly in a cycle which does not include 1. 

Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = set()
        while True:
            if n not in tmp:
                tmp.add(n)
                n = sum([int(x)*int(x) for x in list(str(n))])
                if n == 1:
                    return True
            else:
                return False
            