max = n = int(input())
i = max_i = 0
while n != 0:
    if n > max:
        max = n
        max_i = i
    i += 1
    n = int(input())
print(max_i)
