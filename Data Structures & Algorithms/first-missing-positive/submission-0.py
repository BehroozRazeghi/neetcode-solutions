class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums = sorted(nums)
        for n in nums:
            if n == res:
                res += 1
        return res