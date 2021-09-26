n=int(input())
dp = []
dp.append(1)
dp.append(4)
dp.append(16)
dp.append(61)

for i in range(n+1):
    if i > 2:
        dp.append(4**(i+1) - 4 * dp[i-2] - 8 *dp [i-3] - 2)

print(dp[n] % 1000000007)