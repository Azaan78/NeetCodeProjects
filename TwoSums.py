"""This solution uses a hashmap to store the difference in the target then map each value to their complement"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap=dict()
        n=len(nums)
        current_id=0

        for i in range(n):
            CurNum=nums[i]
            diff=target-CurNum
            if CurNum in hmap:
                return [hmap[CurNum],i]
            else:
                hmap[diff]=i
