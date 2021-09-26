n=int(input())
s=list(input())	
s2 = s[:]

l=[0]
cnt1=0
for i in range(len(s)):
    if(s[i] == "#"):
        cnt1 +=1
    l.append(cnt1)
ansl=[]
for i in range(len(l)):
    ansl.append(n-i-cnt1+2*l[i])



print(min(ansl))