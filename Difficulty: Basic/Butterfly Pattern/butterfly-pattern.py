n = int(input())

for i in range(1, n):
    stars = "*" * i
    spaces = " " * (2 * (n - i) - 1)
    print(stars + spaces + stars)

print("*" * (2 * n - 1))

for i in range(n - 1, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i) - 1)
    print(stars + spaces + stars)