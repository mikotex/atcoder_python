deg = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
dis = [0.0, 0.25, 1.55, 3.35, 5.45, 7.95, 10.75, 13.85, 17.15, 20.75, 24.45, 28.45, 32.65]
x,y = map(int,input().split())	

degindex = int((x + 112.5)/(3600/16))
disindex = 0
for i in range(len(dis)):
    if y/60.0 >= dis[i]:
        disindex = i

if disindex == 0:
    print("C 0")
else:
    print(deg[degindex], disindex)

