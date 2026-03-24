"""
Q1. Excel Column Number

Problem Description
Given a column title as appears in an Excel sheet,
 return its corresponding column number.

Problem Constraints
1 <= length of the column title <= 5

Input Format
The only argument is a string that represents the column title
 in the excel sheet.
Output Format
Return a single integer that represents the corresponding column number.

Example Input
Input 1:
 AB
Input 2:
 BB

Example Output
Output 1:
 28
Output 2:
 54

Example Explanation
Explanation 1:
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
Explanation 2:
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
 ...
 AZ -> 52
 BA -> 53
 BB -> 54
"""
class Solution:
	# @param A : string
	# @return an integer
    def titleToNumber(self, A):
        result = 0
        for char in A:  # Use 'A' instead of 's'
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
s = Solution()
print(s.titleToNumber("AB"))  # Output: 28
print(s.titleToNumber("BB"))  # Output: 54
