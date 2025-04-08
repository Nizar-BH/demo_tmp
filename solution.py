def abbreviate_words() -> str:
    n = int(input())
    for _ in range(n):
        word = input().strip()
        if len(word) > 10:
            return (f"{word[0]}{len(word) - 2}{word[-1]}")
        else:
            return (word)