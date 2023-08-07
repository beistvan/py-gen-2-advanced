n = int(input())

q1, q2, q3, q4 = 0, 0, 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0: q1 += 1
    if x < 0 and y > 0: q2 += 1
    if x < 0 and y < 0: q3 += 1
    if x > 0 and y < 0: q4 += 1

print("1st quadrant: %d" % q1)
print("2nd quadrant: %d" % q2)
print("3rd quadrant: %d" % q3)
print("4th quadrant: %d" % q4)
