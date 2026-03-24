"""
Q1. Majority Element
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109

Input Format
Only argument is an integer array.
Output Format
Return an integer.

Example Input
Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]

Example Output
Input 1:
2
Input 2:
1

Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n=len(A)
        cnt=0
        ele=0
        for i in range(n):
            if i == 0 or ele == 0:
                ele=A[i]
                cnt=1
            elif A[i] == ele:
                cnt += 1
            elif A[i] != ele and cnt > 1:
                cnt -= 1
            elif A[i] != ele and cnt == 1:
                cnt = 0
                ele=0
        return ele
s=Solution()
A=[2, 1, 2]
print(s.majorityElement(A))
A=[1, 1, 1]
print(s.majorityElement(A))
