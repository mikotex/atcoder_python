import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
dish = [a, b, c, d, e]
tmp = 10
for i in range(len(dish)):
    s = dish[i] % 10
    if s < tmp and s != 0:
        tmp = s
sum = 0
for i in range(len(dish)):
    sum += math.ceil(dish[i]/10.0)*10

print(sum - 10 + tmp)