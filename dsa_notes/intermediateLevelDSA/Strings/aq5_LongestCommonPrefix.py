"""
Q5. Longest Common Prefix

Problem Description
Given the array of strings A, you need to find the longest string S,
 which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the
 longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.
Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:
A = ["abab", "ab", "abcd"];

Example Output
Output 1:
"a"
Output 2:
"ab"

Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".
Explanation 2:
Longest common prefix of all the strings is "ab".
"""
class Solution:
    def longestCommonPrefix(self, A):
        if not A:
            return ""

        # Find the shortest string; LCP cannot be longer than this
        shortest = min(A, key=len)
        n = len(shortest)

        # Check each character position
        for i in range(n):
            ch = shortest[i]
            for s in A:
                if s[i] != ch:
                    return shortest[:i]   # up to the previous position

        # Whole shortest string is a common prefix
        return shortest
s = Solution()
A = ["abcdefgh", "aefghijk", "abcefgh"]
print(s.longestCommonPrefix(A))
A = ["abab", "ab", "abcd"]
print(s.longestCommonPrefix(A))
