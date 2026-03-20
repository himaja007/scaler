"""
Q1. Counting Subarrays Easy

Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

Problem Constraints
1 <= N <= 5 x 103
1 <= A[i] <= 1000
1 <= B <= 107

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return an integer denoting the number of subarrays in A having sum less than B.

Example Input
Input 1:
 A = [2, 5, 6]
 B = 10
Input 2:
 A = [1, 11, 2, 3, 15]
 B = 10

Example Output
Output 1:
 4
Output 2:
 4

Example Explanation
Explanation 1:
 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
Explanation 2:
 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}

Expected Output
Provide sample input and click run to see the correct output
 for the provided input. Use this to improve your problem understanding
 and test edge cases
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A, B):
        current_sum=0
        prefix_list=[]
        prefix_list.append(0)
        count_subarray=0
        # print(A)
        # print(B)
        for i in range(len(A)):
            current_sum=current_sum+A[i]
            prefix_list.append(current_sum)
        # print(prefix_list)
        for i in range(len(A)+1):
            for j in range(i,len(A)+1):
                if(i!=j):
                    # print("array indices",i-1,j-1)
                    # print(prefix_list[i],prefix_list[j])
                    # print("prefix_list[j] - prefix_list[i]",prefix_list[j]-prefix_list[i-1])
                    crs=prefix_list[j]-prefix_list[i]
                    if(crs < B):
                        count_subarray+=1
                        # print("count incremented")
        return count_subarray

s=Solution()
print(s.solve([2, 5, 6],10))
print(s.solve([1, 11, 2, 3, 15],10))
print(s.solve([1, 11, 2, 3, 15],20))
print(s.solve([1, 11, 2, 3, 15],30))