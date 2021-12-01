a = int(input())
b = int(input())
for i in range(a, b if a > b else b, a):
    print(i)
