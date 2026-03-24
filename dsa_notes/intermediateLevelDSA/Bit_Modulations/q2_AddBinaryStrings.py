"""
Q2. Add Binary Strings

Problem Description
Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.
Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"

Example Output
Output 1:
"111"
Output 2:
"1000"

Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
The sum of 110 and 10 is 1000.
"""

class Solution:
    def addBinary(self, A, B):
        i = len(A) - 1
        j = len(B) - 1
        carry = 0
        result = []
        while i >=0 or j >=0 or carry:
            bitA = int(A[i]) if i>=0 else 0
            bitB = int(B[j]) if j>=0 else 0
            total = bitA + bitB + carry
            result.append(str(total%2))
            carry = total // 2
            i -= 1
            j -= 1
        return "".join(reversed(result))

s=Solution()
A = "100"
B = "11"
print(s.addBinary(A, B))
A = "110"
B = "10"
print(s.addBinary(A, B))
      