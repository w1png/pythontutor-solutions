data = list(map(int, input().split()))
for i in range(1, len(data), 2):
    data[i], data[i - 1] = data[i - 1], data[i]
print(' '.join(map(str, data)))