class Solution:
    def largest(self, arr):
        # code here
        
        if len(arr) == 1:
            return arr[0]
        i,j=0,len(arr)-1
        while i<j :
            if arr[i]<=arr[j]:
                i+=1
            else:
                j-=1
        return arr[i]
        

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    res = obj.largest(arr)

    print(res)