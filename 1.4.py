n = int(input('please give a positive integer: '))
if n > 0:
    p = 1 # product
    k = n
    for k in range(2, n + 1):
        p *= k # p = p * k
    print(f'{n}! = {p}')
else:
    print('given integer is not positive')