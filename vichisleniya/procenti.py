P, x, y = int(input()), int(input()), int(input())
total = int((x * 100 + y) + (x * 100 + y) * P / 100)
print(total // 100, total % 100)
