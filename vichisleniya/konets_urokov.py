l = int(input())
odd = l // 2
even = (l - 1) // 2
time = l * 45 + odd * 5 + even * 15
print(time // 60 + 9, time % 60)


# l = int(input())
# time = l * 45 + l // 2 * 5 + (l - 1) // 2 * 15
# print(time // 60 + 9, time % 60)

