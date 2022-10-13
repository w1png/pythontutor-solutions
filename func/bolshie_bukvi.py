def capitalize(word: str) -> str:
    return chr(ord(word[0]) - 32) + word[1:]
    
print(" ".join(map(capitalize, input().split())))
