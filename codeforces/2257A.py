for _ in range(int(input())):
	w = set()
	nm = list(map(int, input().split()))
	for i in range(nm[0]):
		w.add(input()[0].upper())
	
	ab = set()
	for i in range(nm[1]):
		ab.update(input())

	print("YES" if ab.issubset(w) else "NO")