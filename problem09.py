def main():
	for a in range(1,500):
		for b in range(a+1, 500):
			c = 1000 - a - b
			if c>b  and (a**2 + b**2 == c**2):
				return a*b*c

if __name__ == '__main__':
	print main()