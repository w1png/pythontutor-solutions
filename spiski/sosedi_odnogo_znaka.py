data = list(map(int, input().split()))
for i in range(1, len(data)):
    if (data[i] > 0 and data[i - 1] > 0) or (data[i] < 0 and data[i - 1] < 0):
        print(data[i - 1], data[i], end=' ')
        break