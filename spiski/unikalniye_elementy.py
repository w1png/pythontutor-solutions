data = list(map(int, input().split()))
print(' '.join(map(str, filter(lambda x: data.count(x) == 1, data))))