from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        diff = 0
        for ind in range(1, n):
            if nums[ind] < nums[ind-1]:
                diff += 1
            if diff > 1:
                return False
        if nums[0] < nums[n-1]:
            diff += 1
        return diff <= 1

if __name__ == "__main__":
    # Sample input: Enter numbers separated by spaces.
    # For example: 3 4 5 1 2
    input_str = input("Enter elements of the array separated by space: ")
    nums = list(map(int, input_str.split()))
    
    obj = Solution()
    result = obj.check(nums)
    print("Result:", result)
