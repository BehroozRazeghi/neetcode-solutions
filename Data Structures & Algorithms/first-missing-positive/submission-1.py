class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # res = 1
        # nums = sorted(nums)
        # for n in nums:
        #     if n == res:
        #         res += 1
        # return res

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums):
                v = nums[i]
                correct_index = v - 1                
                if nums[correct_index] == v:
                    break
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1