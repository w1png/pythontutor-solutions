data = list(map(int, input().split()))
height = int(input())

for i, value in enumerate(data):
    if value < height:
        print(i + 1)
        break
