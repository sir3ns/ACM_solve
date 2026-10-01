def main():
	n = int(input())
	a = list(map(int, input().split()))
	x = 101
	flag = True
	for i in range(n):
		if a[i] != i+1:
			if a[i] < x: x = a[i]
			else:
				flag = False
				break

	if flag: print("YES")
	else: print("NO")


for _ in range(int(input())):
	main()