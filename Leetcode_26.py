from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print("Before:", nums)
        i, j = 0, 1
        size = len(nums)
        while j < size:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        
        print("After:", nums)
        return i + 1

# Testing the function with various inputs
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    input_str = input("Enter elements of the array separated by space: ")
    nums = list(map(int, input_str.split()))
    new_length1 = sol.removeDuplicates(nums)
    print("New Length:", new_length1)
    print("Modified List:", nums[:new_length1])
    print()