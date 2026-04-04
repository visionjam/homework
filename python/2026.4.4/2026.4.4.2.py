def fun(m):
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int(m ** 0.5) + 1, 2):
        if m % i == 0:
            return False
    return True
for num in range(2, 101):
    if fun(num):
        print(num, end=' ')