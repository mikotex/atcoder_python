s=list(input())	

ans1 = 0
for i in range(len(s)):
    if (i % 2 == 0 and s[i] == "0"):
        ans1 +=1
    elif i % 2 == 1 and s[i] == "1":
        ans1 += 1

print(min(ans1, len(s) - ans1))