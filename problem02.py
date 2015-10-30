def sum_even_fib(limit):
	f = 0
	n = 1
	s = 0
	while f < limit:
		f, n = n+f, f
		if f%2 == 0:
			s+=f
	return s

print sum_even_fib(4000000)