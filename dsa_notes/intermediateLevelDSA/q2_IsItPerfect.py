"""
Q2. Is It Perfect?
Problem Description
Given the Number of Test Cases as T,
For each test case, take an integer N as input, you have to tell whether 
it is a perfect number or not.
A perfect number is a positive integer that is equal to the sum of
its proper positive divisors (excluding the number itself). 
A positive proper divisor divides a number without leaving any remainder.

Problem Constraints
1 <= T <= 10
1 <= N <= 106

Input Format
The first line of the input contains a single integer T. 
Each of the next T lines contains a single integer N.

Output Format
For each testcase, print YES if the given integer is perfect,
else print NO, in a separate line

Example Input
Input 1:
2
4
6
Input 2:
1
3

Example Output
Output 1:
NO
YES 
Output 2:
NO

Example Explanation
Explanation 1:
For the first test case A = 4, 
the answer is "NO" as sum of its proper divisors = 1 + 2 = 3, is not equal to 4.
For the second test case A = 6,
the answer is "YES" as sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6.
Explanation 2:
For the first test case A = 3,
the answer is "NO" as sum of its proper divisors = 1, is not equal to 3.

"""
def main():
    N=int(input())
    for i in range(N):
        A=int(input())
        sum=0
        for i in range(1,A):
            if(A%i==0):
                sum+=i
        if(sum==A):
            print('YES')
        else:
            print('NO')



    return 0

if __name__ == '__main__':
    main()
