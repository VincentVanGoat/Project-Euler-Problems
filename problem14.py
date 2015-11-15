def collatz_length(n):
	length = 1
	while n != 1:
		if n%2 == 0:
			n = int(n/2)
		else:
			n = int(3*n+1)
		length += 1
	return length

def main():
	max_length = 1
	max_term = 1
	for i in range(1,1000001):
		length = collatz_length(i)
		if length > max_length:
			max_length = length
			max_term = i
	print max_term

if __name__ == '__main__':
	main()