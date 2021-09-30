#Array Sum
"""
Given an array of length N, you need to find and print the sum of all elements of the array.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :
Sum
"""
Sample Input :
3
9 8 9
Sample Output :
26

Solution :
n=int(input())
li=[int(x) for x in input().split()]
sum = 0
for list_ele in li:
    sum=sum+list_ele
print(sum)


#Swap Alternate
"""
You have been given an array/list(ARR) of size N. 
You need to swap every pair of alternate elements in the array/list.
You don't need to print or return anything, just change in the input array itself.

Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the elements of the resulting array in a single row separated by a single space.
Output for every test case will be printed in a separate line.

"""
Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4
Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2 :
3 9 12 6 32 4 11 5 19
2 1 4 3

Solution :
def swappairwise(li):
  l = len(li)&-2
  li[1:l:2],li[:l:2] = li[:l:2],li[1:l:2]
n=int(input())
li=[int(x) for x in input().split()]
swappairwise(li)
for x in li:
    print(x,end=" ")


#Find Unique
"""
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the unique element present in the array.
Output for every test case will be printed in a separate line.

"""
Sample Input 1:
1
7
2 3 1 6 3 6 2
Sample Output 1:
1
Sample Input 2:
2
5
2 4 7 2 7
9
1 3 1 3 6 6 7 10 7
Sample Output 2:
4
10

Solution :
def find_unique(li):
    ele = li[0]
    for i in range(1, len(li)):
        ele = ele ^ li[i]
    return ele
n = int(input())
li = [int(x) for x in input().split()]
unique = find_unique(li)
print(unique)


#Find Duplicate
"""
You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). 
Each number is present at least once.
That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these,
there is a single integer value that is present twice. 
You need to find and return that duplicate number present in the array.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
For each test case, print the duplicate element in the array/list.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
9
0 7 2 5 4 7 1 3 6
Sample Output 1:
7
Sample Input 2:
2
5
0 2 1 3 1
7
0 3 1 5 4 3 2
Sample Output 2:
1
3

Solution :
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
n = int(input())
list1 = [int(x) for x in input().split()]
for x in Repeat(list1):
    print(x, end=" ")


#Array Intersection
"""
You have been given two integer arrays/list(ARR1 and ARR2) of size M and N, respectively.
You need to print their intersection; 
An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, 
when there is a common value that exists in both the arrays/lists.

Note :
Input arrays/lists can contain duplicate elements.
The intersection elements printed would be in the order they appear in the first array/list(ARR1)

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first the array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

Output format :
For each test case, print the intersection elements in a row, separated by a single space.

Output for every test case will be printed in a separate line.
"""
Sample Input 1 :
2
6
2 6 8 5 4 3
4
2 3 4 7
2
10 10
1
10
Sample Output 1 :
2 4 3
10
Sample Input 2 :
1
4
2 6 1 2
5
1 2 3 4 2
Sample Output 2 :
2 1 2
Explanation for Sample Output 2 :
Since, both input arrays have two '2's, the intersection of the arrays also have two '2's.
The first '2' of first array matches with the first '2' of the second array.
Similarly, the second '2' of the first array matches with the second '2' if the second array.

Solution :
m=float(input())
lst1=[int(x) for x in input().split()]
n=float(input())
lst2=[int(x) for x in input().split()]
for i in range (len(lst1)):
    for j in range (len(lst2)):
        if lst1[i]==lst2[j]:
            print(lst1[i])
            lst2[j]=float("-inf")
            break


#Pair Sum
"""
You have been given an integer array/list(ARR) and a number X.
Find and return the total number of pairs in the array/list which sum to X.

Note:
Given array/list can contain duplicate elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of pairs present in the array/list.

Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2
Explanation for Input 2:
Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.
For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).

Solution :
n = int(input())
a = [int(x) for x in input().split()]
sum = int(input())
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]+a[j]==sum:
            if(a[i]<a[j]):
                print(a[i]," ",a[j])
            else:
                print(a[j]," ",a[i])


#Triplet Sum
"""
You have been given a random integer array/list(ARR) and a number X.
Find and return the triplet(s) in the array/list which sum to X.

Note :
Given array/list can contain duplicate elements.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.

Output format :
For each test case, print the total number of triplets present in the array/list.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
1 2 3 4 5 6 7
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5
Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.
For the second query, we have 5 triplets in total that sum up to 10.
They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)

Solution :
n = int(input())
a = [int(x) for x in input().split()]
sum = int(input())
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):

            if a[i] + a[j] + a[k] == sum:

                if (a[i] <= a[j] <= a[k]):
                    print(a[i], " ", a[j], " ", a[k])

                elif (a[k] <= a[j] <= a[i]):
                    print(a[k], " ", a[j], " ", a[i])

                elif (a[k] <= a[i] <= a[j]):
                    print(a[k], " ", a[i], " ", a[j])

                elif (a[i] <= a[k] <= a[j]):
                    print(a[i], " ", a[k], " ", a[j])

                elif (a[j] <= a[i] <= a[k]):
                    print(a[j], " ", a[i], " ", a[k])

                elif (a[j] <= a[k] <= a[i]):
                    print(a[j], " ", a[k], " ", a[i])


#Sort 0 1
"""
You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1.
Write a function to sort this array/list.
Think of a solution which scans the array/list only once and don't require use of an extra array/list.

Note:
You need to change in the given array/list itself. Hence, no need to return or print anything.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers(all 0s and 1s) representing the elements in the array/list.

Output format :
For each test case, print the sorted array/list elements in a row separated by a single space.
Output for every test case will be printed in a separate line.
"""
Sample Input 1:
1
7
0 1 1 0 1 0 1
Sample Output 1:
0 0 0 1 1 1 1
Sample Input 2:
2
8
1 0 1 1 0 1 0 1
5
0 1 0 1 0
Sample Output 2:
0 0 0 1 1 1 1 1
0 0 0 1 1

Solution :
def count(li):
    total_one=0
    total_zero = 0
    for ele in li:
        if ele == 1:
            total_one+=1
        else:
            total_zero+=1
    return [total_one, total_zero]
n=int(input())
li=[int(x) for x in input().split()]
total_array=count(li)
finalArray = []
for i in range(total_array[1]):
    finalArray.append(0)
for i in range (total_array[0]):
    finalArray.append(1)
for x in finalArray:
    print(x,end=" ")
