class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0

        for i in range(len(nums)):
            
            count = 0

            for j in range(i , len(nums)):
                
                if nums[j] != 0:
                    count += 1
                else:
                    break

            res = max(res, count)

        return res

              
        