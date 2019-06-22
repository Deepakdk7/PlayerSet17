ax=int(input())
a=[]
c=0
for i in range(0,ax):
    a.append(input())
for i in range(0,len(a)):
    if 'a' in a[i] or 'e' in a[i] or 'i' in a[i] or 'o' in a[i] or 'u' in a[i]:
        c=c+1
    else:
        print('no')
        break
if c==len(a):
    print('yes')
