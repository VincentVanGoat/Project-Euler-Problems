#This seems slow. :(

def largest_palindrome():
	max = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			n = i*j
			s = str(n)
			if s == s[::-1] and n > max:
				max = n
	return max

print largest_palindrome()