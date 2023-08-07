lst = list(map(int, input().split()))
print(sum((1 for i, k in enumerate(lst) if i < len(lst) - 1 and lst[i] < lst[i + 1])))
