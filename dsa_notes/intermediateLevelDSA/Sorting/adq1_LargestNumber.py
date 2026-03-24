"""
Q1. Largest Number

Problem Description
Given an array A of non-negative integers, arrange them such that they
 form the largest number.
Note: The result may be very large, so you need to return a string
 instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format
The first argument is an array of integers.

Output Format
Return a string representing the largest number.

Example Input
Input 1:
 A = [3, 30, 34, 5, 9]
Input 2:
 A = [2, 3, 9, 0]

Example Output
Output 1:
 "9534330"
Output 2:
 "9320"

Example Explanation
Explanation 1:
Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:
Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.
"""
# class Solution:
#     # @param A : list of integers
#     # @return a strings
#     def largestNumber(self, A):
#         A.sort(reverse=True)
#         c=""
#         sum_A=sum(A)
#         for i in A:
#             if(sum_A>0):
#                 c=c+str(i)
#             else:
#                 c = 0
#         return c

class Solution:
    # @param A : list of integers
    # @return a string
    def largestNumber(self, A):
        # Convert all integers to strings for proper comparison
        A = list(map(str, A))
        
        # Custom sort: compare x+y vs y+x for every pair
        A.sort(key=lambda x: x*10, reverse=True)
        
        result = ''.join(A)
        
        # Handle all zeroes: if leading char is zero, result is "0"
        return '0' if result[0] == '0' else result

s = Solution()
A = [3, 30, 34, 5, 9]
print(s.largestNumber(A))
A = [2, 3, 9, 0]
print(s.largestNumber(A))
