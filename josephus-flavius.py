def k(n, m):
    if n == 1:
        return 1
    else:
        return 1 + (k(n - 1, m) + m - 1) % n

n, m = int(input()), int(input())
print(k(n, m))
