def trianglize(n):
	return n * (n+1)//2

def pentagonalize(n):
	return n * (3*n - 1)//2

def hexagonalize(n):
	return n * (2*n - 1)

def main():
	pentagons = set(pentagonalize(n) for n in range(100000))
	hexagons = set(hexagonalize(n) for n in range(100000))
	for n in range(100000):
		t = trianglize(n)
		if t in pentagons and t in hexagons and t > 40755:
			print t

if __name__ == '__main__':
	main()
