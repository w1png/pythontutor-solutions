n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

m, max_index = 0, (0, 0)

for i, current_list in enumerate(l):
    for j, current_element in enumerate(current_list):
        if current_element > m:
            m = current_element
            max_index = (i, j) 

print(*max_index)
