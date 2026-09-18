for _ in range(int(input())):
	input()
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	x = a[-1]
	for i in range(len(a)-1):
		x = x + ( a[i] - a[i+1] + 1 )

	y = b[-1]
	for i in range(len(b)-1):
		y = y + ( b[i] - b[i+1] + 1 )

	print(1 if x >= y else 2)