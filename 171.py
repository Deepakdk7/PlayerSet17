ax=input().split()
for i in range(0,len(ax)):
    if len(ax)<3:
        break
    if ax[i]=='and':
        t=ax[i-1]
        ax[i-1]=ax[i+1]
        ax[i+1]=t
print(*ax)
