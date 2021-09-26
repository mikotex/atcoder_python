a,b,c = map(int,input().split())	

if (a<c and b> c):
    print("Yes")
elif (a>c and b<c):
    print("Yes")
else:
    print("No")