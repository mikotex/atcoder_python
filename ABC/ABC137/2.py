x,y = map(int,input().split())	

ansli=[]
for i in range (x * 2 - 1):
    ans = y - x + i + 1
    if (ans <= 1000000 and ans >= -1000000):
        ansli.append(ans)

for i in range(len(ansli)):
    print(ansli[i], end = "")
    if i != len(ansli) -1:
        print(" ", end="")
print("")