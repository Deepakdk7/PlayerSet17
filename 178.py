ax=list(input())
c=[]
for i in range(0,len(ax)):
    for j in range(i+1,len(ax)):
        if ax[i]==ax[j]:
            c.append(ax[i].upper())
for i in ax:
    if i.upper() in c:
        print(i.upper(),end='')
    else:
        print(i,end='')
