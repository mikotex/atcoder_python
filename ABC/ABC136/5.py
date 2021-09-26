def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse =True)
    return divisors

n,k = map(int,input().split())

li = list(map(int,input().split()))

sumli = sum(li)

div =make_divisors(sumli)
for i in range(len(div)):
    ans = div[i]
    diff =list(map(lambda x: x % ans, li))
    for i in range(len(diff)):
        if (ans - diff[i] < diff[i]):
            diff[i] = - (ans - diff[i])
    a = sum(diff)
    diffabs = list(map(lambda x:max(x, -x), diff))
    b = sum(diffabs)
    absa = max(a, -a)
    if ((b - absa)/2 + absa <= k):
        print(ans)
        print(a)
        print(b)
        break