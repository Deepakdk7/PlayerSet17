ax=list(input())
a=[];b=[];c=[];e=[];d=0
for i in ax:
    if i==' ':
        ax.remove(' ')
    elif i not in a:
        a.append(i)
for i in a:
    for j in range(0,len(ax)):
        if i==ax[j]:
            c.append(ax.count(i))
            b.append(ax.count(i))
            b.append(i)
d=max(c)
print(d,end=' ')
for i in range(0,len(b)):
    if b[i]==d and b[i+1] not in e:
        e.append(b[i+1])
print(*e,sep='')
