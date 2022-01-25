# 1
data = list(map(int, input().split()))
k, c = map(int, input().split())

data.insert(k, c)
print(' '.join(map(str, data)))


# 2
data = list(map(int, input().split()))
k, c = map(int, input().split())

data.append(data[-1])
for i in range(len(data) - 1, k, -1):
    data[i], data[i - 1] = data[i - 1], data[i]
data[k] = c

print(' '.join(map(str, data)))

