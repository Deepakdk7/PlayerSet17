ax=input().split()
c=0
for j in range(0,len(ax)):
    for i in ax[j]:
        c=c+1
for i in range(2,c):
    if c%i==0:
        print('no')
        break
else:
    print('yes')
