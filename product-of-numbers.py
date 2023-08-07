from itertools import combinations

arr = [int(input()) for _ in range(int(input()))]
p = int(input())
isProd = False
for a, b in combinations(arr, 2):
    isProd = a * b == p
    if isProd: break
print("yes" if isProd else "no")
