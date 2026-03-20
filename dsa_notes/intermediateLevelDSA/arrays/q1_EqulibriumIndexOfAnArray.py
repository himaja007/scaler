class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        left=0
        right=0
        N=len(A)

        #create right sum starting from1 to N-1 keeping 0 as initial index
        for i in range(1,N):
            right+=A[i]
        
        for i in range(N):
            if i!=0:
                left+=A[i-1]
                right-=A[i]

            if right==left:
                return i
        
        return -1
s=Solution()
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([1, 2, 3, 4, 6]))
print(s.solve([1, 2, 3, 4, 10]))
print(s.solve([1, 2, 3, 4, 11]))
print(s.solve([1, 2, 3, 4, 15]))
print(s.solve([1, 2, 3, 4, 16]))
