"""
Q5. Shaggy and distances
Problem Description

Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

Problem Constraints
1 <= |A| <= 105

Input Format
The first and only argument is an integer array A.

Output Format
Return one integer corresponding to the minimum possible distance between a special pair.

Example Input
Input 1:
A = [7, 1, 3, 4, 1, 7]
Input 2:
A = [1, 1]


Example Output
Output 1:
 3
Output 2:
 1
Example Explanation
Explanation 1:
Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3. 
Explanation 2:
Only possibility is choosing A[1] and A[2].
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases

"""

class Solution:
    # @param A : List of integers
    # @return an integer
    def solve(self, A):
        last_seen = {}
        min_distance = float('inf')
        for i in range(len(A)):
            if A[i] in last_seen:
                min_distance = min(min_distance, i - last_seen[A[i]])
            last_seen[A[i]] = i
        return -1 if min_distance == float('inf') else min_distance
s = Solution()
print(s.solve([7, 1, 3, 4, 1, 7]))  # Output: 3
print(s.solve([1, 1]))  # Output: 1
