"""
Q2. Monkeys and Doors
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
There are 100 doors, all closed. In a nearby cage are 100 monkeys.

The first monkey is let out and runs along the doors opening every one. The second monkey is then let out and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors. The third monkey is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. After all 100 monkeys have done their work in this way, what state are the doors in after the last pass?

Answer with the number of open doors.

Answer is an integer (without any spaces). Just put the number without any decimal places if it's an integer. If the answer is Infinity, output Infinity.

Feel free to get in touch with us if you have any questions
"""

"""
Number are being flipped at their factors. Ideally Open → 
Close i.e Even will close and Odd will open. So Numbers having odd 
factors will be Opened. We know that Perfect square number is having odd
factor whereas Other number doesn’t. Prime number have (1*2,1*3, 1*5 etc). 
Even → 1*6, 2*3. Odd → 1*15, 3*5. Square → 16, 1*16, 2*8, 4*4 (Count == 5) """