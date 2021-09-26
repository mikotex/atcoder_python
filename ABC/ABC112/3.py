n = int(input())
x=[]
y=[]
h=[]
for i in range(0,n):
    a,b,c = map(int,input().split())
    x.append(a)
    y.append(b)
    h.append(c)
 
 
 
for i in range(0,101):
    for j in range(0,101):
        tmph=0
        flag = True
        for k in range(0,n):
            if tmph == 0 and h[k] != 0:
                tmph=abs(x[k]-i)+abs(y[k]-j)+h[k]
                break
        for k in range(0,n):
            calch = tmph - abs(x[k]-i)-abs(y[k]-j)
            if h[k] != max(calch,0):
                flag = False
                break
        if flag == False:
            continue
        elif tmph == 0:
            flag2 = True
            for c in range(0,101):
                if i == x[c] and j == y[c]:
                    flag2 = False
                    break
            if flag2:
                ansx = i
                ansy = j
                ansh = 1
        else:
            ansx=i
            ansy=j
            ansh=tmph
 
print(ansx,ansy,ansh)