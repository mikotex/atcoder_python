n,q = map(int,input().split())
#s=list(input())	
s = input()
index = -1
indexes = []
while True:
    index = s.find("AC", index + 1)
    if index == -1:
        break
    indexes.append(index)
dp = []

for i in range (n):
    dp.append(len(indexes))
    if len(indexes)> 0 and indexes[0] == i:
        indexes.pop(0)
for i in range(q):
    l,r = map(int,input().split())
    print(dp[l-1] - dp[r-1])

