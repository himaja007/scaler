"""
Q1. Is It Prime?
Problem Description
Take an integer A as input, you have to tell whether it is a prime number or not.
A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
Problem Constraints
1 <= A <= 106

Input Format
First and only line of the input contains a single integer A.

Output Format
Print YES if A is a prime, else print NO.
Example Input
Input 1:
 3 
Input 2:
 4 

Example Output
Output 1:
 YES 
Output 2:
 NO 

Example Explanation
Explanation 1:
 3 is a prime number as it is only divisible by 1 and 3.
Explanation 2:
 4 is not a prime number as it is divisible by 2.

"""
import math
def main():
    num=int(input())
    count=0
    for i in range(1,int(math.sqrt(num))):
        if(num % i ==0):
            count=count+2
        else:
            count=count+0
    
    if(count==2):
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == '__main__':
    main()