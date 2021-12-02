from math import sqrt
x = int(input())
all_nums = list()
sd_summ = s_summ = 0
while x != 0:
    s_summ += x
    all_nums.append(x)
    x = int(input())
s = s_summ / len(all_nums)
for x in all_nums:
    sd_summ += (x - s) ** 2
print(sqrt(sd_summ / (len(all_nums) - 1)))
    
