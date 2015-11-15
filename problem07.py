import math

def isprime(n):
	if n<0:
		return False
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i == 0:
			return False
	return True

prime = []
i = 1

while len(prime)<= 10001:
	i += 1
	if isprime(i):
		prime.append(i)

print prime[10000]