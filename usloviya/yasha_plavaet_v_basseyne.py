# яша плавает в бассейне
a = int(input()) 
b = int(input()) 
x = int(input()) 
y = int(input()) 

# a - длинная, b - короткая
if b > a:
    a, b = b, a


if a == y or a == x:
    print(0)
elif b - x > y < a - y or b - x > x < a - y:
    print(min(x, y))
elif b - x < x and b - x < a - y:
    print(b - x)
elif a - y < y and a - y < b - x:
    print(a - y)
else:
    print(min(x, y))

