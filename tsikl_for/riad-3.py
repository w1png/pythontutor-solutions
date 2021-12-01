a = int(input())
b = int(input())
for i in range(a + a % 2 - 1, b - b % 2 - 1, -2):
    print(i, end=" ")
