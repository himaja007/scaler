"""
Problem Description
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.


NOTE:


Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.


Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109



Input Format

First argument is an integer array A of size N.

Second argument is an integer array B of size M.



Output Format

Return an integer array denoting the common elements.



Example Input

Input 1:

 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:

 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]


Example Output

Output 1:

 [1, 2, 2]
Output 2:

 [2, 10]


Example Explanation

Explanation 1:

 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:

 Elements (2, 10) appears in both the array.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: An Integer Array, For e.g [1,2,3]
Enter Input Here
Arg 2: An Integer Array, For e.g [1,2,3]
Enter Input Here
"""
# Approach 1: Brute Force
"""A =[1, 2, 2, 1]
B= [2, 3, 1, 2]
new_list=[]
for i in A:
    for j in B:
        if i==j:
            new_list.append(i)
            B.remove(j)
print(new_list)"""

"""# Approach 2: Using Hashing
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        from collections import Counter

        freqA = Counter(A)
        freqB = Counter(B)
        ans = []

        # iterate over smaller map for speed
        if len(freqA) > len(freqB):
            freqA, freqB = freqB, freqA

        for x in freqA:
            if x in freqB:
                k = min(freqA[x], freqB[x])
                ans.extend([x] * k)

        return ans"""


#Approach 3:
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freq_B = {}
        for x in B:
            if x in freq_B:
                freq_B[x] += 1
            else:
                freq_B[x] = 1

        lst = []
        for x in A:
            if x in freq_B and freq_B[x] > 0:
                lst.append(x)
                freq_B[x] -= 1

        return lst

A=[1, 2, 2, 1,3]
B= [2, 3, 1, 2,3]
s = Solution()
print(s.solve(A,B))