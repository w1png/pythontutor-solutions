#cards = set()
#for i in range(int(input()) - 1):
#    cards.add(int(input()))
#print(list(({j for j in range(1, i + 3)} - cards))[0])
n = int(input())
print(list(({j for j in range(1, n + 1)} - {int(input()) for _ in range(n - 1)}))[0])

