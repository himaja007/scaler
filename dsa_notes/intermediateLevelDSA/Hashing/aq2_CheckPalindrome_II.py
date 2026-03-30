"""
Q2. Check Palindrome - II

Problem Description
Given a string A consisting of lowercase characters.
Check if characters of the given string can be rearranged to form a palindrome.
Return 1 if it is possible to rearrange the characters of the string A such 
that it becomes a palindrome else return 0.

Problem Constraints
1 <= |A| <= 105
A consists only of lower-case characters.

Input Format
First argument is an string A.

Output Format
Return 1 if it is possible to rearrange the characters of the string A such
that it becomes a palindrome else return 0.

Example Input
Input 1:
 A = "abcde"
Input 2:
 A = "abbaee"


Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No possible rearrangement to make the string palindrome.
Explanation 2:
 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.

Expected Output
Provide sample input and click run to see the correct output for the provided
input. Use this to improve your problem understanding and test edge cases
"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq = {}
        
        for ch in A:
            freq[ch] = freq.get(ch, 0) + 1
        
        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1
        
        return 1 if odd_count <= 1 else 0
s = Solution()
A = "abcde"
print(s.solve(A))  # Output: 0
A = "abbaee"
print(s.solve(A))  # Output: 1
A = "aabbcc"
print(s.solve(A))  # Output: 1 (can be rearranged to "abcabc")
A = "aabbccd"
print(s.solve(A))  # Output: 1 (can be rearranged to "abcdcba")
A = "aabbccdd"
print(s.solve(A))  # Output: 1 (can be rearranged to "abcdcdba")
A = "aabbccdde"
print(s.solve(A))  # Output: 0 (more than one character has odd frequency)
