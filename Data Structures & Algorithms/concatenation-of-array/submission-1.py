class Solution:
    def getConcatenation(self, nums: List[int], k=2) -> List[int]:
        ans = []
        for i in range(k):
            for n in nums:
                ans.append(n)

        return ans
        