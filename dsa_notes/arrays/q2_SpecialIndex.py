"""
Q2. Special Index

Problem Description
Given an array, arr[] of size N, the task is to find the count of
 array indices such that removing an element from these indices
 makes the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105
Sum of all elements of A <= 109

Input Format
First argument contains an array A of integers of size N
Output Format
Return the count of array indices such that removing an element
 from these indices makes the sum of even-indexed and odd-indexed
 array elements equal.

Example Input
Input 1:
A = [2, 1, 6, 4]
Input 2:
A = [1, 1, 1]

Example Output
Output 1:
1
Output 2:
3

Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.
"""

class Solution:
    def solve(self, A):
        n = len(A)
        prefEven = [0] * n
        prefOdd = [0] * n

        # Build prefix sums
        for i in range(n):
            if i == 0:
                prefEven[i] = A[i]
                prefOdd[i] = 0
            else:
                prefEven[i] = prefEven[i-1]
                prefOdd[i] = prefOdd[i-1]
                if i % 2 == 0:
                    prefEven[i] += A[i]
                else:
                    prefOdd[i] += A[i]

        totalEven = prefEven[n-1]
        totalOdd = prefOdd[n-1]

        count = 0
        for i in range(n):
            # sums before i
            even_before = prefEven[i-1] if i > 0 else 0
            odd_before = prefOdd[i-1] if i > 0 else 0

            # sums after i (with parity flipped)
            even_after = totalOdd - prefOdd[i]
            odd_after = totalEven - prefEven[i]

            even_sum = even_before + even_after
            odd_sum = odd_before + odd_after

            if even_sum == odd_sum:
                count += 1

        return count
s=Solution()
print(s.solve([2, 1, 6, 4]))
print(s.solve([1, 1, 1]))
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([1, 2, 3, 4, 5, 6]))
