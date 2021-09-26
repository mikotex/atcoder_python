n,m = map(int,input().split())	
bait={}
for i in range(n):
    x,y = map(int,input().split())
    if x in bait:
        bait[x].append(y)
    else:
        bait[x]=[]
        bait[x].append(y)

ans=0
for i in range(m):
    maxtmp = 0
    for j in range(i + 1):
        if j+1 in bait and len(bait[j+1]) > 0:
            tmp = max(bait[j+1])
            if(maxtmp < tmp):
                maxtmp = tmp
                index = bait[j+1].index(tmp)
                bait[j+1].pop(index)
                break
    ans += maxtmp
print(ans)
        

