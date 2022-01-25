# TODO: maybe make this shorter

data = list(map(int, input().split()))

mi = data.index(min(data))
ma = data.index(max(data))
data[mi], data[ma] = data[ma], data[mi] 

print(' '.join(map(str, data)))