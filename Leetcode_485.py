#485. Max Consecutive Ones
#simply count the max number of occurences of 1

class Solution:
    def findMaxConsecutiveOnes(self,nums):
        count=0
        max_count=0
        for num in nums:
            if num==1:
                count+=1
                #print(f'for num {num} the count is {count} and max_xount is {max_count}')
            elif num==0:
                count=0
                #print(f'for num {num} the count is {count} and max_xount is {max_count}')
            max_count=max(count,max_count)
        return max_count
nums = [1,0,1,1,0,1]
sol=Solution()
result=sol.findMaxConsecutiveOnes(nums)
print(result)