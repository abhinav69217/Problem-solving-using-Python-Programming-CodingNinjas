n = int(input())
upper_part = (n+1)//2
lower_part = n // 2
'''upper part'''
i = 1
while i <= upper_part:
    b = 1
    while b <= upper_part-i:
        print(" ", end="")
        b = b+1
    j = 1
    while j <= (2*i)-1:
        print("*", end="")
        j = j+1
    print()
    i = i+1
'''lower part'''
i = lower_part
while i >= 1:
    b = 1
    while b <= lower_part-i+1:
        print(" ", end="")
        b = b+1
    j = 1
    while j <= 2*i-1:
        print("*", end="")
        j = j+1
    print()
    i = i-1
