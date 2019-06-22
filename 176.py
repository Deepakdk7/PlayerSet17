ax=input().split()
a=list(ax[0])
b=list(ax[1])
a=list(dict.fromkeys(a))
b=list(dict.fromkeys(b))
a.sort()
b.sort()
if a==b:
    print('true')
else:
    print('false')
