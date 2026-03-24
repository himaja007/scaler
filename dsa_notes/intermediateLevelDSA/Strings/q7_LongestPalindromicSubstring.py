"""
Q7. Longest Palindromic Substring
Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)
Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints
1 <= N <= 6000

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
Input 1:
A = "aaaabaaa"
Input 2:
A = "abba

Example Output
Output 1:
"aaabaaa"
Output 2:
"abba"

Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".
"""
class Solution:
    # @param A : string
    # @return string
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return A

        start = 0
        end = 0

        def expand(l, r):
            # expand while within bounds and characters match
            while l >= 0 and r < n and A[l] == A[r]:
                l -= 1
                r += 1
            # when loop breaks, palindrome is from l+1 to r-1
            return l + 1, r - 1

        for i in range(n):
            # odd length palindrome centered at i
            l1, r1 = expand(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            # even length palindrome centered at i, i+1
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return A[start:end + 1]
s = Solution()
A = "aaaabaaa"
print(s.longestPalindrome(A))
A = "abba"
print(s.longestPalindrome(A))
