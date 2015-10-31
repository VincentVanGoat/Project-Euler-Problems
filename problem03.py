import math

def is_prime(n):
    if n < 0:
        return False
    for f in range(2, int(math.sqrt(n))+1):
        if n%f == 0:
            return False
    return True

num = 600851475143

arr = []

for i in range(1,int(math.sqrt(num))+1):
	if num%i == 0 and is_prime(i):
		arr.append(i)

print max(arr)