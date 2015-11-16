def factorial(n):
	fact = 1
	for i in range(1,n+1):
		fact *= i
	return fact

fact_sum = 0

for j in str(factorial(100)):
	fact_sum += int(j)

print fact_sum