for _ in range(int(input())):
	input()
	a = list(map(int, input().split()))
	if a.count(0) <= a.count(1):
		print("Bessie")
	else:
		print("Elsie")