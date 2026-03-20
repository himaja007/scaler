"""Q4. Sub-array with 0 sum
Unsolved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9
Input Format
The only argument given is the integer array A.
Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]

Input 2:
 A = [4, -1, 1]

Example Output
Output 1:
 0
Output 2:
 1
Example Explanation
Explanation 1:
 No subarray has sum 0.
Explanation 2:
 The subarray [-1, 1] has sum 0.
Expected Output
Provide sample input and click run to see the correct output for 
the provided input. Use this to improve your problem understanding and 
test edge cases

eg: [1,2,3,-3,4,-4]"""

class Solution:
    def solve(self, A):
        prefix = 0
        seen = set()
        for x in A:
            prefix += x
            if prefix == 0 or prefix in seen:
                return 1
            seen.add(prefix)
        return 0
s=Solution()
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([4, -1, 1]))
print(s.solve([1,2,3,-3,4,-4]))