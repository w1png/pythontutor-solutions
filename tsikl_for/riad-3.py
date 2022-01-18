a, b = int(input()), int(input())
print(" ".join([str(i) for i in range(a + a % 2 - 1, b - b % 2 - 1, -2)]))
