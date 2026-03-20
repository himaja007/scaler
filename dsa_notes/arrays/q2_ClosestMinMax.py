"""
Q2. Closest MinMax

Problem Description

Given an array A, find the size of the smallest subarray such
 that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Return the length of the smallest subarray which has at
 least one occurrence of minimum and maximum element of the array

Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [2, 6, 1, 6, 9]

Example Output
Output 1:
 2
Output 2:
 3

Example Explanation
Explanation 1:
 Take the 1st and 2nd elements as they are the minimum and
 maximum elements respectievly.
Explanation 2:
 Take the last 3 elements of the array.

"""



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        inf = 100000000000
        min_ele=min(A)
        max_ele=max(A)
        last_min=-inf
        last_max=-inf/2
        result=inf
        c=0
        for i in A:
            if(i == min_ele):
                last_min=c
            if(i == max_ele):
                last_max=c
            p=abs(last_min - last_max) + 1
            if(result > p):
                result=p
            c=c+1
            ###result = min(result, abs(last_min - last_max) + 1)
        return result
    

s=Solution()
print(s.solve([1, 3, 2]))
print(s.solve([2, 6, 1, 6, 9]))
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([1, 2, 3, 4, 5, 6]))
print(s.solve([1, 1, 1, 1, 1]))