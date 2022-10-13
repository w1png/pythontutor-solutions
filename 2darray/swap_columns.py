n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
i, j = map(int, input().split())

def swap_columns(l, i, j):
    for row in l:
        row[i], row[j] = row[j], row[i]

swap_columns(l, i, j)
for i in range(n):
    print(" ".join(map(str, l[i])))
