def solve(a, b):
	print(a, end= ' ')
	if a <= 0:
		return 
	solve(a-b, b)
	print(a, end= ' ')


solve(10,5)
print()
solve(16,5)
print()
solve(12,3)
print()
