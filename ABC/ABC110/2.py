li = [int(i) for i in input().split()] 

x = [int(i) for i in input().split()] 
y = [int(i) for i in input().split()] 
x.append(li[2])
y.append(li[3])

x.sort()
y.sort()
if((int(x[-1])) <int(y[0])):
    print('No War')
else:
    print('War')

