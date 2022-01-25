data = list(map(int, input().split()))
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        print(data[i], end=' ')