n = int(input())
n1 = 0
n2 = iter = 1
result = -1
while n2 <= n:
    if n2 == n:
        result = iter
    n3 = n1 + n2
    n1, n2, n3 = n2, n3, 0
    iter += 1
print(result)
