"""
Q2. Star Pattern I

Problem Description
Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.
See example for clarifications over the pattern.

Problem Constraints
1 <= N <= 1000

Input Format
First line is an integer N

Output Format
N lines conatining only char '*' as per the question.

Example Input
Input 1:
4
Input 2:
6

Example Output
Output 1:
********
***  ***
**    **
*      *
*      *
**    **
***  ***
********
Output 2:
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(1, N + 1):
        # Printing stars from i to N
        for j in range(i, N + 1):
            print('*', end='')
        # Printing spaces
        spaces = 2 * i - 2
        for j in range(spaces):
            print(' ', end='')
        # Printing stars again from i to N
        for j in range(i, N + 1):
            print('*', end='')
        # Moving to the next line after each row
        print()

    # Second half of the pattern
    for i in range(1, N + 1):
        # Printing stars from 1 to i
        for j in range(1, i + 1):
            print('*', end='')
        # Printing spaces
        spaces = 2 * (N - i)
        for j in range(spaces):
            print(' ', end='')
        # Printing stars again from 1 to i
        for j in range(1, i + 1):
            print('*', end='')
        # Moving to the next line after each row
        print()

    return 0

if __name__ == '__main__':
    main()