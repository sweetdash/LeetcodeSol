#873. Length of Longest Fibonacci Subsequence

from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        check={}
        max_len=0

        #Create a map to look up the elements. It will be helpful while finding the fibbonaci pattern number
        for i in range(len(arr)):
            if arr[i] in check:
                check[arr[i]]+=1
            else:
                check[arr[i]]=1
        #check the length of the every possible subarray
        for ol1 in range(len(arr)):
            for ol2 in range(ol1+1,len(arr)):
                prev1,prev2=arr[ol1],arr[ol2] #First two characters of the fibbonacci series
                length=2
                while prev1+prev2 in check: #checking if there exists a third element in the given array by using the map
                    length+=1
                    max_len=max(max_len,length)
                    prev1,prev2=prev2,prev1+prev2 # updating the value to find fourth and so on elements
        return max_len if max_len>2 else 0
    

sol=Solution()
arr=[1,3,7,11,12,14,18]
result=sol.lenLongestFibSubseq(arr)
print(result)
