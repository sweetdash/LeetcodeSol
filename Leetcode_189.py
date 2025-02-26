#189.Rotate Array


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_ele_pos=0
        prev=0
        size=len(nums)
        count=0
        start=0
        while count<size: #maintains the cycles
            current=start
            prev=nums[start]
            while True:
                new_ele_pos=(current+k)%size
                nums[new_ele_pos],prev=prev,nums[new_ele_pos]
                current=new_ele_pos
                count+=1
                if current==start:
                    break
            start+=1
        print(nums)

arr=[1,2,3,4,5,6,7]
k=3
sol = Solution()
output = sol.rotate(arr,k)

