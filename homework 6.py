w = int(input('give the weight: '))

if w <= 2:
    p = 3
elif 2 < w <= 5:
    p = 2 + (w - 2)*2
else:
    p = 8 + (w - 5)*3

print(f'the price is {p}')

