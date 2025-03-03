#268. Missing Number
# a^a=0 and a^0=a

class Solution:
    def missingNumber(self,nums):
        res=len(nums)
        for i,num in enumerate(nums):
            res=res^(i^num)
        return res
sol=Solution()
nums = [9,6,4,2,3,5,7,0,1]
result=sol.missingNumber(nums)
print(result)
