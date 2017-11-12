def power(a, n):
    b = a
    if a < 0:
        return 'Incorrect number'
    if n > 0:
        for i in range(n-1):
            a *= b
        return 'Result is: '+str(a)
    elif n == 0:
        return 'Result is: '+str(1)
    else:
        for i in range(abs(n)-1):
            a *= b
        return 'Result is: '+str(1/a)
print(power(float(input('a:')), int(input('n:'))))
