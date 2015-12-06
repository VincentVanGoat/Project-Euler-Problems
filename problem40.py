digits = ''.join(str(digit) for digit in range(1,1000001))
d = [int(digit) for digit in digits]
print d[0] * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999]
# Prints 210