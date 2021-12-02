n = int(input())
if n == 0:
    print(0)
else:
    n1 = 0
    n2 = 1
    for i in range(n - 1):
        n3 = n1 + n2
        n1, n2, n3 = n2, n3, 0
    print(n2)
