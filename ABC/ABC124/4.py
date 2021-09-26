import numpy as np
n,k = map(int,input().split())	
s=list(input())	

li = []
is1s = False
if s[0] == "1":
    is1s = True
cnt0 = 0
cnt1 = 0
for i in range(len(s)):
    if s[i] == "0" :
        cnt0 += 1
    elif s[i] == "1":
        cnt1 += 1
    if i >= 1:
        if s[i] == "0" and s[i-1] == "1":
            li.append(cnt1)
            cnt1 = 0
        elif s[i] == "1" and s[i-1] == "0": 
            li.append(cnt0)
            cnt0 = 0

if (cnt1 > 0):
    li.append(cnt1)
if (cnt0 > 0):
    li.append(cnt0)
pivot = 2 * k 
li = np.array(li)
anslist=[]
if(is1s):
    for i in range(len(li)):
        if(i % 2 == 0):
            tmp = np.sum(li[i:min(len(li), i+pivot+1)])
            anslist.append(tmp)
else:
    for i in range(len(li)):
        if(i % 2 == 1):
            tmp = np.sum(li[i:min(len(li), i+pivot+1)])
            anslist.append(tmp)
    anslist.append(sum(li[0:pivot]))

print(max(anslist))

