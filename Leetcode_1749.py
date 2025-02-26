#1749. Maximum Absolute Sum of Any Subarray

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_int=0
        max_int=0
        prefix_sum=0
        n=len(nums)
        for i in range(n):
            prefix_sum+=nums[i]
            min_int=min(min_int,prefix_sum)
            max_int=max(max_int,prefix_sum)
        return max_int-min_int
# **Define Input**
nums = [2, -5, 1, -4, 3, -2]
k = -4

# **Run the Function**
solution = Solution()
output = solution.maxAbsoluteSum(nums, k)

# **Print Output**
print(f"Maximum Absolute Sum of Any Subarray : {output}")