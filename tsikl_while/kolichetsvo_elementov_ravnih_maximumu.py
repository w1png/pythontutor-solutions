max = n = int(input())
same = 0
while n != 0:
    if n > max:
        max = n
    elif n == max:
        same += 1
    n = int(input())
print(same)
