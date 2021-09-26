s=list(input())	
tmp = 0
ans = 0
for word in s:
    if word == "A":
        tmp += 1
    elif word == "T":
        tmp += 1
    elif word == "G":
        tmp += 1
    elif word == "C":
        tmp += 1
    else:
        tmp = 0
    if ans < tmp :
        ans = tmp

print(ans)
