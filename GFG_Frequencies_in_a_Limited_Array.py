#This problem has 2 solutions with second one being most effective

#Normal solution with O(n) time complexity and O(n) space complexity

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        if len(arr)==0:
            return [0]
        if len(arr)==1:
            return [1]
        res={}
        for i in arr:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        for j in range(len(arr)):
            if j+1 in res:
                arr[j]=res[j+1]
            else:
                arr[j]=0
        return arr
            
if __name__ == "__main__":

    arr = list(map(int, input().split()))  # Read input array
    s = Solution().frequencyCount(arr)  # Compute frequencies
    print(" ".join(map(str, s)))  # Print the result

#optimized solution with O(n) time complexity and O(1) space complexity

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        
        m=len(arr)+1 # multiplier
        n=len(arr)
        for i in range(n):
            val=arr[i]%m # it might be possible that the element was modified in the beginninh and again found in other index
            if val>0:
                arr[val-1]+=m
        for i in range(n):
            arr[i]=arr[i]//m
        return arr
if __name__ == "__main__":

    arr = list(map(int, input().split()))  # Read input array
    s = Solution().frequencyCount(arr)  # Compute frequencies
    print(" ".join(map(str, s)))  # Print the result
