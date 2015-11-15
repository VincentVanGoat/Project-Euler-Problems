def main():
	sum_of_digits = 0
	for i in str(2**1000):
		sum_of_digits += int(i)

	print sum_of_digits

if __name__ == '__main__':
	main()