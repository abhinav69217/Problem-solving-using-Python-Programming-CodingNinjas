#Fahrenheit to Celsius Function
"""
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
you need to convert all Fahrenheit values from Start to End at the gap of W,
into their corresponding Celsius values and print the table.

Input Format :
3 integers - S, E and W respectively

Output Format :
Fahrenheit to Celsius conversion table.
One line for every Fahrenheit and Celsius Fahrenheit value.
Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
"""
Sample Input 1:
0
100
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37
Sample Input 2:
120
200
40
Sample Output 2:
120 48
160 71
200 93

Solution :
s=int(input())
e=int(input())
st=int(input())
def conversion(start,end,step):
    for f in range(start,end,step):
        cel=int((f-32)*5/9)
        print(str(f)+"\t"+str(cel))
conversion(s,e,st)


#Fibonacci Member
"""
Given a number N, figure out if it is a member of fibonacci series or not. 
Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence
        F(n) = F(n-1) + F(n-2)
     where F(0) = 0 and F(1) = 1

Input Format :
Integer N

Output Format :
true or false
"""
Sample Input 1 :
5
Sample Output 1 :
true

Sample Input 2 :
14
Sample Output 2 :
false

Solution :
def checkMemberNPrint(n):
    curr = 1
    prev = 1
    while (curr < n):
        temp = curr + prev
        prev = curr
        curr = temp
    if curr == n:
        print("true")
    else:
        print("false")

n = int(input())
checkMemberNPrint(n)


#Palindrome number
"""
Write a program to determine if given number is palindrome or not. 
Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
"""
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false

Solution :
n = int(input())
nclone = n
rev = 0
while n > 0:
    l = n % 10
    n = n//10
    rev = rev * 10 + l
if nclone == rev:
    print("true")
else :
    print("false")


#Check Armstrong
"""
Write a Program to determine if the given number is Armstrong number or not. 
Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) 
such that the sum of its digits raised to nth power is equal to the number itself.

For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

Input Format :
Integer n
Output Format :
true or false

"""
Sample Input 1 :
1
Sample Output 1 :
true
Sample Input 2 :
103
Sample Output 2 :
false

Solution :
num = int(input())
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print("true")
else:
   print("false")
