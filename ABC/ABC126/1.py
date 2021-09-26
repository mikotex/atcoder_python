x,y = map(int,input().split())	
s=input()	
print(s[:y-1] + s[y-1].lower() + s[y:])