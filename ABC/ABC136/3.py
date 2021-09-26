a=int(input())

li = list(map(int,input().split()))

li.reverse()

mins = 100000000000

isyes = True
for i in li:
    if i < mins:
        mins = i
    
    if i - mins > 1:
        isyes=False

if(isyes):
    print('Yes')
else:
    print('No')
