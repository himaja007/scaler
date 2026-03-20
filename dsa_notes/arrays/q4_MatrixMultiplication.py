"""
Q4. Matrix Multiplication

Problem Description
You are given two integer matrices A(having M X N size) and B(having N X P).
 You have to multiply matrix A with B and return the resultant matrix.
 (i.e. return the matrix AB).
Matrix Multiplication 
Problem Constraints
1 <= M, N, P <= 100
-100 <= A[i][j], B[i][j] <= 100

Input Format
The first argument given is the 2-D integer matrix A.
The second argument given is the 2-D integer matrix B.
Output Format
Return a 2D integer matrix denoting AB.

Example Input
Input 1:
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
Input 2:
A = [[1, 1]]
B = [[2],
     [3]]

Example Output
Output 1:
 [[19, 22],
  [43, 50]]
Output 2:
 [[5]]
Example Explanation
Explanation 1:
 is the number of rows in A and j is the number of columns in B,
 then AB[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + ... + A[i][N-1] * B[N-1][j].
Explanation 2:
 [[1, 1]].[[2], [3]] = [[1 * 2 + 1 * 3]] = [[5]]

"""

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]
s=Solution()
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
print(s.solve(A,B))
A = [[1, 1]]
B = [[2],
     [3]]
print(s.solve(A,B))
