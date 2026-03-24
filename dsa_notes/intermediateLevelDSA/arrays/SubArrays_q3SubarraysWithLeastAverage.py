"""
Q3. Subarray with least average

Problem Description
Given an array A of size N, find the subarray of size B with the least average.

Problem Constraints
1 <= B <= N <= 105
-105 <= A[i] <= 105

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.

Output Format
Return the index of the first element of the subarray of size B that has
 least average.
Array indexing starts from 0.

Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:
A = [3, 7, 5, 20, -10, 0, 12]
B = 2

Example Output
Output 1:
3
Output 2:
4

Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:
 Subarray between [4, 5] has minimum average
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A, B):
        prefix_sum_list=[]
        prefix_sum_list.append(0)
        current_sum=0
        current_avg=0
        
        s_i=0
        e_i=B
        f_s_i=0
        for i in range(len(A)):
            current_sum=current_sum+A[i]
            prefix_sum_list.append(current_sum)
        min_avg=prefix_sum_list[len(A)]
        while(s_i>=0 and e_i<=len(A)):
            current_sum=prefix_sum_list[e_i]-prefix_sum_list[s_i]
            current_avg=int(current_sum/3)
            if(min_avg>current_avg):
                min_avg=current_avg
                f_s_i=s_i
            s_i+=1
            e_i+=1
        return (f_s_i)
s=Solution()
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
print(s.solve(A, B))
A = [3, 7, 5, 20, -10, 0, 12]
B = 2
print(s.solve(A, B))
A = [3, 7, 90, 20, 10, 50, 40]
B = 4
print(s.solve(A, B))
