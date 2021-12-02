n = int(input())
max = max2 = 0
while n != 0:
    if n > max:
        max2 = max
        max = n
    elif n > max2 and max > n:
        max2 = n
    n = int(input())
print(max2)
