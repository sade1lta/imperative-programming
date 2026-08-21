n = 1
found = False

while not found:
    if (n**3 - 16) % 47 == 0:
        found = True 
    else:
        n = n + 1

print(n)