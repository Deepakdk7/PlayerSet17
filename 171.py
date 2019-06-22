ax=input().split()
for i in range(0,len(ax)):
    if ax[i]=='and':
        t=ax[i-1]
        ax[i-1]=ax[i+1]
        ax[i+1]=t
print(*ax)
