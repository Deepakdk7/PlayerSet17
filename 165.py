def A(k):
    for i in a:
        if k==i:
            print(k)
            break
    else:
        k=k+1
        A(k)
bx=list(map(int,input().split()))
a=list(map(int,input().split()))
k=bx[1]
A(k)
