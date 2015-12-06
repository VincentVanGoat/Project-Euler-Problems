def trianglize(n):
	return int(0.5 * n * (n+1))

words = [word.strip('"') for word in open('words.txt').read().split(',')]
triangle_numbers = [trianglize(i) for i in range(1, 100)]
counter = 0
for word in words:
	if sum((ord(w) - 64) for w in word) in triangle_numbers:
		counter += 1

print counter