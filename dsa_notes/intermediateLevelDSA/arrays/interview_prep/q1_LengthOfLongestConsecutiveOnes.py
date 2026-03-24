"""
Q1. Length of longest consecutive ones

Given a binary string A. It is allowed to do at most one swap
 between any 0 and 1. Find and return the length of the longest
 consecutive 1’s that can be achieved.

Input Format
The only argument given is string A.

Output Format
Return the length of the longest consecutive 1’s that can be achieved.

Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example
Input 1:
    A = "111000"
Output 1:
    3
Input 2:
    A = "111011101"
Output 2:
    7
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        max_cons = 0
        total_one = len([i for i in A if i== '1'])  # get overall number of 1 in given string

        if total_one == n: # when all the string is 1 . Ex : 1111111
            return total_one

        for i in range(n):

            left = 0
            right = 0
            if A[i] == "1": # Skip if it is 1
                continue

            for j in range(i - 1, -1,-1): # Get number of 1’s from the left side until we found 0
                if A[j] == "1":                    
                    left += 1
                    swap_require = 1
                else:
                    break
            
            for j in range(i + 1, n): # Get number of 1’s from the right side until we found 0
                if A[j] == "1":                    
                    right += 1
                else:
                    break
            
            curr_total = left + right

            if curr_total > 0 and max_cons < (curr_total + 1):
                if total_one == curr_total: # When there is no extra 1’s to swap Ex :. 0111110110 or 00001111
                    max_cons = curr_total
                else:
                    max_cons = left + right +1
            
        return max_cons
s=Solution()
A = "111000"
print(s.solve(A))
A = "111011101"
print(s.solve(A))
