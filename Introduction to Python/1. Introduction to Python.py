#Find average Marks
"""
Write a program to input marks of three tests of a student (all integers).
Then calculate and print the average of all test marks.
"""
a = int(input())
b = int(input())
c = int(input())
Average = (a + b + c) / 3
print(Average)


#Find X raised to power N
"""
You are given two integers: X and N. 
You have to calculate X raised to power N and print it.
"""
X = int(input())
N = int(input())
Output = X**N
print(Output)


#Arithmetic Progression
"""
You are given first three entries of an arithmetic progression.
You have to calculate the common difference and print it.
"""
a = int(input())
b = int(input())
c = int(input())
d = b - a
#or
d = c - b
print(d)


#Rectangular Area
"""
You are given a rectangle in a plane. The corner coordinates of this rectangle is provided to you.
You have to print the amount of area of the plane covered by this rectangles.
The end coordinates are provided as four integral values: x1, y1, x2, y2.
It is given that x1 < x2 and y1 < y2.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
Area = (x2 - x1) * (y2 - y1)
print(Area)
