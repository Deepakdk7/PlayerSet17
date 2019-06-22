ax=list(map(int,input().split()))
a=list(bin(ax[0]^ax[1]))
c=0
for i in a:
    if i=='1':
        c=c+1
print(c)
