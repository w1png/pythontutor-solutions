def power(a: float, n: int) -> None:
    result = 1
    for i in range(abs(n)):
        result *= a
    return 1 if n == 0 else (result if n > 0 else 1 / result)

print(power(*map(int, [input() for _ in range(2)])))
