n=int(input())
strli=[]
for i in range(n):
    li=list(input())
    strli.append(li)

strs=[]
for i in range (n):
    strli[i].sort()
    strs.append("".join(strli[i]))

cnt = {}
for i in range(n):
    if strs[i] in cnt:
        cnt[strs[i]] += 1
    else:
        cnt[strs[i]] = 1
ans = 0
for i in cnt:
    if cnt[i] >= 2:
        ans += int(cnt[i] * (cnt[i] -1) /2)

print(ans)