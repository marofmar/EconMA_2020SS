"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = []
        idx = 0
        while len(nums) > idx:
            if nums[idx] not in tmp:
                tmp.append(nums[idx])
                idx += 1
            else:
                tmp.remove(nums[idx])
                idx += 1
        return tmp[0]
# But this was way too slow and O(n^2) time complexity

# Better solution is to use Hash table, way faster
from collections import defaultdict
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int) 
        for i in nums:
            hash_table[i] += 1
        for j in hash_table:
            if hash_table[j] == 1:
                return j
