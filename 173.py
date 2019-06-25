ax=input()
bx=input()
a=[]
if ' ' in ax and ' ' in bx:
    ax=ax.split()
    bx=bx.split()
    if len(ax)>len(bx):
        for i in ax:
            if i not in bx:
                a.append(i)
    else:
        for i in bx:
            if i not in ax:
                a.append(i)
    print(*a)
else:
    ax=list(ax)
    bx=list(bx)
    mi=min(len(ax),len(bx))
    ma=max(len(ax),len(bx))
    for i in range(0,mi):
        if ax[i]!=bx[i]:
            a.append(ax[i])
            a.append(bx[i])
    for i in range(mi,ma):
        if len(ax)>len(bx):
            a.append(ax[i])
        else:
            a.append(bx[i])
    print(*a)
