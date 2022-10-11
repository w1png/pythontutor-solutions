n = int(input())

l = list()
for i in range(n):
    l.append([i for i in range(i, 0, -1)] + [i for i in range(n - i)])

for i in range(n):
    print(" ".join(map(str, l[i])))
