"""
Q4. Square root of a number
Problem Description
Given a number A.
Return square root of the number if it is perfect square otherwise return -1.
Note: A number is a perfect square if its square root is an integer.
Problem Constraints
1 <= A <= 108
Input Format
First and the only argument is an integer A.
Output Format
Return an integer which is the square root of A if A
 is perfect square otherwise return -1.
Example Input
Input 1:
A = 4
Input 2:
A = 1001
Example Output
Output 1:
2
Output 2:
-1

Example Explanation
Explanation 1:
sqrt(4) = 2
Explanation 2:
1001 is not a perfect square.

Expected Output
Provide sample input and click run to see the correct output for the 
provided input. Use this to improve your problem understanding and test 
edge cases
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A < 1 or A > 10**8:
            return "Invalid Input, expected 1 <= A <= 10^8"

        low=1
        high=A 
        
        while low <= high:
            mid=(low+high)//2
            i= mid * mid 
            if i > A:
                high = mid -1
            elif i < A:
                low = mid + 1
            elif i == A:
                return mid 
        return -1 
s=Solution()
print(s.solve(4)) # 2
print(s.solve(1001)) # -1
print(s.solve(1)) # 1