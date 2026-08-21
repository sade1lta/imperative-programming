a = int(input('give a nonnegative integer: '))
b = int(input('give a integer: '))

answer1 = 1

for i in range(a):
    answer1 = answer1 * 3

print(answer1)

answer2 = 1

for v in range(a):
    answer2 = answer2 * b

print(answer2)