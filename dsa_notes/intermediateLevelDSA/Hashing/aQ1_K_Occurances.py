"""
Groot has N trees lined up in front of him where the height of the i'th 
tree is denoted by H[i].
He wants to select some trees to replace his broken branches.
But he wants uniformity in his selection of trees.
So he picks only those trees whose heights have frequency B.
He then sums up the heights that occur B times. 
(He adds the height only once to the sum and not B times).
But the sum he ended up getting was huge so he prints it modulo 10^9+7.
In case no such cluster exists, Groot becomes sad and prints -1.

Constraints:
1.   1<=N<=100000
2.   1<=B<=N
3.   0<=H[i]<=10^9
Input: Integers N and B and an array C of size N
Output: Sum of all numbers in the array that occur exactly B times.

Example:
Input:
N=5 ,B=2 ,C=[1 2 2 3 3]
Output:
5
Explanation:
There are 3 distinct numbers in the array which are 1,2,3.
Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 
which is 5.
Expected Output
Provide sample input and click run to see the correct output for the provided 
input. Use this to improve your problem understanding and test edge cases
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):
        mod = 10**9 + 7
        freq = {}
        for i in range(A):
            if C[i] in freq:
                freq[C[i]] += 1
            else:
                freq[C[i]] = 1

        ans = 0
        found = False          # track if any value has frequency B
        for key, value in freq.items():
            if value == B:
                found = True
                ans = (ans + key) % mod

        return ans if found else -1

s = Solution()
N = 5
B = 2
C = [1, 2, 2, 3, 3]
print(s.getSum(N, B, C))  # Output: 5
N = 6
B = 3
C = [1, 1, 2, 2, 3, 3]
print(s.getSum(N, B, C))  # Output: -1
N = 7
B = 2
C = [1, 1, 2, 2, 3, 3, 4]
print(s.getSum(N, B, C))  # Output: 10 (1 + 2 + 3 + 4)
N = 8
B = 1
C = [1, 2, 3, 4, 5, 6, 7, 8]
print(s.getSum(N, B, C))  # Output: 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
