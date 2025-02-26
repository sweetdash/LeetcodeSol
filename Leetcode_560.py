#560. Subarray Sum Equals K
#use prefix sum to solve it
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        max_len = 0
        prefix_sum = 0
        check = {0: 1}  # Dictionary to store prefix sum frequencies
        count = 0
        n = len(nums)

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum - k in check:
                count += check[prefix_sum - k]  # Count occurrences

            check[prefix_sum] = check.get(prefix_sum, 0) + 1  # Store/update prefix sum

        return count

# **Define Input**
nums = [2, -5, 1, -4, 3, -2]
k = -4

# **Run the Function**
solution = Solution()
output = solution.subarraySum(nums, k)

# **Print Output**
print(f"Number of subarrays with sum {k}: {output}")
