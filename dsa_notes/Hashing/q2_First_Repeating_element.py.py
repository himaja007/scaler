"""
Q2. First Repeating element
Unsolved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

Given an integer array A of size N, find the first repeating element in it.






We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.








Problem Constraints

1 <= N <= 105

1 <= A[i] <= 109



Input Format

The first and only argument is an integer array A of size N.



Output Format

Return an integer denoting the first repeating element.



Example Input

Input 1:

 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:

 A = [6, 10, 5, 4, 9, 120]


Example Output

Output 1:

 5
Output 2:

 -1


Example Explanation

Explanation 1:

 5 is the first element that repeats
Explanation 2:

 There is no repeating element, output -1



Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: An Integer Array, For e.g [1,2,3]
Enter Input Here
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self,A):
        seen = set()
        ans = -1
    # iterate from right to left
        for x in reversed(A):
            if x in seen:
                ans = x
            else:
                seen.add(x)
        return ans

A=[10, 5, 3, 4, 3, 5, 6]
s=Solution()
print(s.solve(A))
A = [6, 10, 5, 4, 9, 120]
print(s.solve(A))
