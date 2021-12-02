n = int(input())
if n == 1:
    print(0, 1)
else:
    result = 2
    power = 1
    while result * 2 <= n:
        result *= 2
        power += 1
    print(power, result)
