n = int(input())
print(list(({j for j in range(1, n + 1)} - {int(input()) for _ in range(n - 1)}))[0])
