a = float(input('Number: '))
n = int(input('Power: '))


def power(a, n):
    if (a < 0) or (n < 0):
        return 'Incorrect number'
    if n == 0:
        return 1
    else:
        return a*power(a, n-1)
print(power(a, n))
