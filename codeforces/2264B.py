from heapq import heappush, heappop

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    heap = []
    ttl = 0

    for x in a[:m-1]:
        heappush(heap, -x)
        ttl += x

    ans = float('-inf')

    for x in a[m-1:]:
        ans = max(ans, m * x - ttl)

        heappush(heap, -x)
        ttl += x

        if len(heap) > m - 1:
            ttl += heappop(heap)

    print(ans)


for _ in range(int(input())):
    main()