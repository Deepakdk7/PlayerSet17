def A(k):
    for i in a:
        if k==i:
            print(k)
            break
    else:
        k=k+1
        A(k)
ax=list(map(int,input().split()))
a=list(map(int,input().split()))
k=ax[1]
A(k)
