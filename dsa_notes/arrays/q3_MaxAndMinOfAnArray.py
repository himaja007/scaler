"""
Q3. Max and Min of an Array

Problem Description
Take input an array A of size N and write a program to print maximum
and minimum elements of the input. The only line of the input would contain
a single integer N that represents the length of the array followed by the
N elements of the input array A.

Problem constraints
1 <= N <= 1000
1 <= A <= 1000

Input Format
The first line contains a single integer N representing the 
length of the array A followed by N elements of the array A.

Output Format
A single line output containing two space-separated integers.
The first integer is the maximum value of the array.
The second integer is the minimum value of the array. 

There is **no space** after the minimum value in the output format. 
There is only a **single space** between the maximum and minimum value.

Example Input
Input 1:
5 1 2 3 4 5
Input 2:
4 10 50 40 80

Example Output
Output 1:
5 1
Output 2:
80 10
"""


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    x = list(map(int, input().split()))
    x.pop(0) # Removing the fist element, which signifies number of elements
    print(max(x), min(x))
    return 0

if __name__ == '__main__':
    main()
