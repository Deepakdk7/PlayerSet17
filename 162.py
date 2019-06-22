ax=list(map(int,input().split()))
k=ax[1]
a=[]
c=0
for i in range(0,ax[0]):
    a.append(input())
for i in range(0,ax[0]):
    if 'a' in a[i] or 'e' in a[i] or 'i' in a[i] or 'o' in a[i] or 'u' in a[i]:
        c=c+1
if c>=k:
    print('yes')
else:
    print('no')
