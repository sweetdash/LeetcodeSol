#283. Move Zeroes

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        i=0
        j=0
        
        while i<size:
            if nums[i]!=0: #keep j idle at begining and search for non zero number. Once found swap it with j and increment the j positon
                nums[i],nums[j]=nums[j],nums[i] 
                j+=1
            i+=1
sol=Solution()
nums=[0,1,0,3,12]
sol.moveZeroes(nums)
print(f'nums:{nums}')