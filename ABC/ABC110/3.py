import collections

s=list(input())
t=list(input())
s = collections.Counter(s)
t = collections.Counter(t)
sc=s.most_common()
tc=t.most_common()
ans = True
for i in range(min(len(sc), len(tc))):
    if sc[i][1] != tc[i][1]:
        ans = False

if(ans):
    print('Yes')
else:
    print('No')
