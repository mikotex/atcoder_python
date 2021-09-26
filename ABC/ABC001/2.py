a=int(input())

if a < 100:
    print('00')
elif a <= 5000:
    ans = a/100
    ans = '%02d' % ans
    print(ans)
elif a <= 30000:
    print(int(a/1000+50))
elif a <= 70000:
    print(int((a/1000-30)/5+80))
else:
    print('89')