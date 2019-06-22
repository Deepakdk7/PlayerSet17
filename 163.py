ax=list(map(int,input().split()))
a=list(map(int,input().split()))
k=ax[1]
for i in a:
    if k==i:
        print('yes')
        break
else:
    print('no')
