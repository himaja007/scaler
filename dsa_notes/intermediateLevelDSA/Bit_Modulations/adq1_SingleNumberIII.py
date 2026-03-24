"""
Q1. Single Number III

Problem Description
Given an array of positive integers A, two integers appear only once,
 and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.
Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The first argument is an array of integers of size N.

Output Format
Return an array of two integers that appear only once.

Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
Input 2:
A = [1, 2]

Example Output
Output 1:
[3, 4]
Output 2:
[1, 2]

Example Explanation
Explanation 1:
3 and 4 appear only once.
Explanation 2:
1 and 2 appear only once.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xo = 0
        for num in A:
            xo ^= num

        # get rightmost set bit in xo
        diff_bit = xo & -xo

        a = 0
        b = 0
        for num in A:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        if a < b:
            return [a, b]
        else:
            return [b, a]
s = Solution()
A = [1, 2, 3, 1, 2, 4]
print(s.solve(A))
