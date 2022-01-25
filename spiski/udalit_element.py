data = list(map(int, input().split()))

for i in range(int(input()), len(data) - 1):
    data[i] = data[i + 1]

data.pop()
print(' '.join(map(str, data)))
