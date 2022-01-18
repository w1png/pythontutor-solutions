a, b = int(input()), int(input())
print(" ".join([str(i) for i in range(min(a, b), max(a, b) + 1)]))
