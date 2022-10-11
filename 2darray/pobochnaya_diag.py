n = int(input())

l = list()
for i in range(n):
    l.append(list(map(int, list("0"*(n-i) + "1" + "2"*i))))

for i in range(n):
    print(" ".join(map(str, l[i])))