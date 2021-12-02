prev = n = int(input())
current_number = None
current_streak = max_streak = 0
while n != 0:
    if n == prev:
        if current_number == None or current_number == n:
            current_number = n
            current_streak += 1
    else:
        if current_streak > max_streak:
                max_streak = current_streak
        current_number = None
        current_streak = 1
    prev = n
    n = int(input())
# костыль на случай, если все числа одинаковые
if current_streak > max_streak:
    max_streak = current_streak
print(max_streak)
