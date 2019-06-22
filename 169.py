ax=list(input())
x=list(dict.fromkeys(ax))
x.sort()
for i in x:
    c=0
    m=i
    for j in ax:
        if m==j:
            c=c+1
    else:
        print(m,end='')
        print(c,end='')
