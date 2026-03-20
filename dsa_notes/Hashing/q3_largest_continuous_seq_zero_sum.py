"""Q3. Largest Continuous Sequence Zero Sum
Unsolved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints

1 <= N <= 106

-107 <= A[i] <= 107



Input Format

Single argument which is an integer array A.



Output Format

Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input

A = [1,2,-2,4,-4]


Example Output

[2,-2,4,-4]


Example Explanation

[2,-2,4,-4] is the longest sequence with total sum of zero.



Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        # Dictionary to store first occurrence of each prefix sum
        prefix_sum_map = {0: -1}  # Initialize with 0 at index -1
        current_sum = 0
        max_length = 0
        start_idx = 0
        end_idx = -1
        
        # Iterate through the array
        for i in range(len(A)):
            current_sum += A[i]
            
            # If prefix sum already exists, we found a zero-sum subarray
            if current_sum in prefix_sum_map:
                length = i - prefix_sum_map[current_sum]
                if length > max_length:
                    max_length = length
                    start_idx = prefix_sum_map[current_sum] + 1
                    end_idx = i
            else:
                # Store first occurrence of this prefix sum
                prefix_sum_map[current_sum] = i
        
        # Return the longest zero-sum subarray
        if max_length == 0:
            return []
        return A[start_idx:end_idx + 1]
s=Solution()
A = [1,2,-2,4,-4]
print(s.lszero(A))
A=[1,2,3,-3,4,-4]
print(s.lszero(A))