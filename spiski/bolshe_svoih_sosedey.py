data = list(map(int, input().split()))
counter = 0
for i in range(1, len(data) - 1):
    if data[i] > data[i - 1] and data[i] > data[i + 1]:
        counter += 1
print(counter)
