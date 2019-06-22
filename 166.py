a1,a2=list(map(int,input().split()))
a=min(a1,a2)
c=1
for i in range(1,a+1):
    c=c*i
print(c)
