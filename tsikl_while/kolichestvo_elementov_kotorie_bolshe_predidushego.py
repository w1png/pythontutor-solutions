prev = n = int(input())
larger = 0
while n != 0:
    if n > prev:
        larger += 1
    prev = n
    n = int(input())
print(larger)
