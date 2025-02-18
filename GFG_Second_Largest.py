#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest=-1
        second =-1
        for num in arr:
            if num>largest:
                second=largest
                largest=num
            elif num>second and num!=largest:
                second=num
        return second

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    ob = Solution()
    ans = ob.getSecondLargest(arr)
    print(ans)