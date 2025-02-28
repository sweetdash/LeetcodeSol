#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        union=[]
        a_size,b_size=len(a),len(b)
        i,j=0,0
        while i<a_size and j<b_size:
            if a[i]<b[j]:
                if not union or union[-1]!=a[i]:
                    union.append(a[i])
                    print("inside less")
                i+=1
                print(union)
            elif a[i]>b[j]:
                if not union or union[-1] != b[j]:
                    union.append(b[j])
                print("inside more")
                j += 1 
                print(union)
            else:
                if not union or union[-1]!=a[i]:
                    union.append(a[i])
                    print("inside equal")
                i+=1
                j+=1
                print(union)
        while i<a_size:
            if union[-1]!=a[i]:
                union.append(a[i])
            i+=1
        while j<b_size:
            if union[-1]!=b[j]:
                union.append(b[j])
            j+=1
        #print(a)
        return union
            

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    #test_cases = int(input())
    #for cases in range(test_cases):
        #a = list(map(int, input().strip().split()))
        #b = list(map(int, input().strip().split()))
    a = [-9, -4, -1, -1, 0, 0, 5, 6, 8]
    b = [-7, -7, -6, -5, 4, 5]
    ob = Solution()
    li = ob.findUnion(a, b)
    for val in li:
        print(val, end=' ')
    print()
    print("~")

# } Driver Code Ends