n, m = map(int, input().split())

board = list()
for i in range(n):
    sym = ".*"
    if i % 2 == 0:
        sym = "*."
    board.append(list((sym*m)[:m]))

for i in range(n):
    print(" ".join(board[i]))
