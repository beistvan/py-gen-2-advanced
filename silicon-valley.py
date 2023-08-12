import re
print(*[i + 1 for i in range(int(input())) if len(re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', input())) > 0])
