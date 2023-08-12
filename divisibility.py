def func(num1, num2):
    return not(num1 % num2)

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print("can be divided")
else:
    print("cannot be divided")
