palindrome = []
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        z = int(x * y)
        a, b = str(z), str(z)[::-1]
        if a == b:
            palindrome.append(z)

print(max(palindrome))
