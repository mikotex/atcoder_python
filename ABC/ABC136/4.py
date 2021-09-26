li=list(input())	

index = []
rindex = []
rindex.append(0)
tmp = 'R'
for i in range(len(li)):
    if (li[i] == 'L' and tmp == 'R'):
        index.append(i)
    if (li[i] == 'R' and tmp == 'L'):
        rindex.append(i)    
    tmp = li[i]


ans=[0] * len(li)

tmpi = 0
for i in range(len(index)):
    if (i == len(index) -1):
        n = len(li) - rindex[i]
        r = len(li)
    else:
        n = rindex[i+1] -rindex[i]
        r = rindex[i+1]
    left = int((index[i] - rindex[i] + 1)/2) + int((r - index[i]) /2) 
    ans[index[i] - 1] = left
    ans[index[i]] = n - left

for i in ans:
    print(str(i) + " ", end="")
print()