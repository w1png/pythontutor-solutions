summ = 0
fact = 1
for i in range(1, int(input()) + 1):
    fact *= i
    summ += fact
print(summ)