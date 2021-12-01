n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
elif n3 < n1 and n3 < n2:
    print(n3)
