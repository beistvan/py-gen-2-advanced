m = float(input())
h = float(input())

ind = m / (h * h)

if 18.5 <= ind <= 25:
    print("Ideal weight")
elif ind < 18.5:
    print("Ubderweight")
else:
    print("Overweight")
