"""
Q4. Range Sum Query
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2,
 where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L
 to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R]
 for each query.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109
0 <= L <= R < N

Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.

Output Format
Return an integer array of length M where ith element is the
 answer for ith query in B.
Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
Input 2:
A = [2, 2, 2]
B = [[0, 0], [1, 2]]

Example Output
Output 1:
[10, 5]
Output 2:
[2, 4]
Example Explanation
Explanation 1:
The sum of all elements of A[0 ... 3] = 1 + 2 + 3 + 4 = 10.
The sum of all elements of A[1 ... 2] = 2 + 3 = 5.
Explanation 2:
The sum of all elements of A[0 ... 0] = 2 = 2.
The sum of all elements of A[1 ... 2] = 2 + 2 = 4.

Expected Output
Provide sample input and click run to see the correct output for
 the provided input. Use this to improve your problem understanding
 and test edge cases

"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        pfx_sum=0
        prefixsum_list=[]
        prefixsum_list.append(0)
        results=[]
        n=len(A)
        for i in range(0,n):
            pfx_sum=pfx_sum+A[i]
            prefixsum_list.append(pfx_sum)
        for j in B:
            return_sum=prefixsum_list[j[1]]-prefixsum_list[j[0]-1]
            results.append(return_sum)
        return results
s=Solution()
print(s.rangeSum([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))
print(s.rangeSum([2, 2, 2], [[0, 0], [1, 2]]))
print(s.rangeSum([1, 2, 3, 4, 5], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]))
print(s.rangeSum([1, 2, 3, 4, 5], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]))
print(s.rangeSum([1, 2, 3, 4, 5], [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]))