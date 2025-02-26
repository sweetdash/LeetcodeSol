# User function Template for python3

class Solution:
        
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        max_len=0
        prefixSum=0
        check={}
        for i in range(n):
            prefixSum+=arr[i]
            
            if prefixSum==k:
                max_len=i+1
            if (prefixSum-k)  in check:
                current_len=i-check[prefixSum-k]
                max_len=max(max_len,current_len)
            if prefixSum not in check:
                check[prefixSum]=i
        return max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends