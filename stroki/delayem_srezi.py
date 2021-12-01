n = input()
print(f"{n[2]}\n{n[-2]}\n{n[:5]}\n{n[:-2]}\n{n[::2]}\n{n[1::2]}\n{n[::-1]}\n{''.join((n[::-1])[i] for i in range(0, len(n), 2))}\n{len(n)}")

