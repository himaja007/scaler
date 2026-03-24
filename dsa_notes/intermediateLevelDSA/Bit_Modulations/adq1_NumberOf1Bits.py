"""
Q1. Number of 1 Bits

Problem Description
Write a function that takes an integer and returns the number of 1 bits
 present in its binary representation.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument contains integer A

Output Format
Return an integer

Example Input
Input 1:
11
Input 2:
6

Example Output
Output 1:
3
Output 2:
2

Example Explanation
Explaination 1:
11 is represented as 1011 in binary.
Explaination 2:
6 is represented as 110 in binary.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        binary = bin(A)
        return (binary.count("1"))
s = Solution()
A = 11
print(s.numSetBits(A))
A = 6
print(s.numSetBits(A))
