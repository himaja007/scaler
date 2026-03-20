"""

Q1. Amazing Subarrays

You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a
 vowel (a, e, i, o, u, A, E, I, O, U).

Input
Only argument given is string S.
Output
Return a single integer X mod 10003, here X is the number of Amazing
 Substrings in given the string.

Constraints
1 <= length(S) <= 1e6
S can have special characters

Example
Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
Expected Output
Provide sample input and click run to see the correct output
 for the provided input. Use this to improve your problem understanding
 and test edge cases

"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        str_list=list(A)
        count=0
        vovels=['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(A)):
            if(A[i]in vovels):
                loacl_count=len(A)-i
                count=count+loacl_count
        return count%10003
s=Solution()
print(s.solve("ABEC"))
print(s.solve("AEIOU"))
print(s.solve("ABCDE"))
print(s.solve("abcde"))
