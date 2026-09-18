def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(a,b):
	return (a // gcd(a,b)) * b


for _ in range(int(input())):
	input()
	l = list(map(int, input().split()))
	print(gcd(l[0], l[-1]))