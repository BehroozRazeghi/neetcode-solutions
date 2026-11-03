class Solution:
    def findMin(self, nums: List[int]) -> int:


        l, r = 0, len(nums) - 1
        res = nums[l] 

        while l <= r:
            
            # if subarray already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # if subarray is not sorted, use binary search
            m = l + (r - l) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # search right side
                l = m + 1
            else: 
                # search left side
                r = m - 1
        return res
         