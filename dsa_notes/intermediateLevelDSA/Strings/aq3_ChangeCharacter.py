"""
Q3. Change character

Problem Description
You are given a string A of size N consisting of lowercase alphabets.
You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
Find the minimum number of distinct characters in the resulting string.

Problem Constraints
1 <= N <= 100000
0 <= B <= N

Input Format
The first argument is a string A.
The second argument is an integer B.

Output Format
Return an integer denoting the minimum number of distinct characters in the string.

Example Input
A = "abcabbccd"
B = 3

Example Output
2

Example Explanation
We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.
"""
class Solution:
    def solve(self, A, B):
        from collections import Counter

        # Count frequency of each character
        cnt = Counter(A)
        freqs = sorted(cnt.values())          # ascending by frequency
        distinct = len(freqs)                 # current distinct characters

        # Greedily remove least frequent characters
        for f in freqs:
            if B >= f:
                B -= f
                distinct -= 1                 # this character can be fully changed
            else:
                break

        # String is non-empty, so at least 1 distinct character will remain
        return max(distinct, 1)
s = Solution()
A = "abcabbccd"
B = 3
print(s.solve(A, B))
