a=int(input())

u = int(a /100)
l = a%100

if (1 <= u <=12 and 1 <= l <= 12):
    print("AMBIGUOUS")
elif (a == 0 or (u == 0 and l > 12) or (l == 0 and u > 12) or (l > 12 and u > 12)):
    print("NA")
elif (1 <= u <= 12):
    print("MMYY")
else:
    print("YYMM")