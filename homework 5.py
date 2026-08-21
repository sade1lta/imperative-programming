a = int(input('give the first integer: '))
b = int(input('give the second integer: '))

if a >= 100:
    if b <=50:
        print(1)
    else:
        print(0)
else:
    print(0)
print()

if a >= 100:
    if b <= 50:
        print(1)
    else:
        print(0)
elif b >= 100:
    if a <= 50:
        print(1)
    else:
        print(0)
else:
    print(0)

