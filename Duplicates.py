"""First project on Neetcode, Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Use set as it removes duplicates, and check lengths
        if len(set(nums))==len(nums):
            return False
        return True
