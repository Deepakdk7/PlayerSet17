a=input()
b=input()
c=['1:']
d=['2:']
if a.isnumeric()==False:
    a=a.split()
    b=b.split()
    for i in a:
        if i not in b:
            d.append(i)
    for i in b:
        if i not in a:
            c.append(i)
else:
    a=list(a)
    b=list(b)
    for i in range(0,max(len(a),len(b))):
        if i<min(len(a),len(b)) and a[i]!=b[i]:
            d.append(a[i])
            c.append(b[i])
        elif i>=min(len(a),len(b)):
            if max(len(a),len(b))==len(a):
                d.append(a[i])
            if max(len(a),len(b))==len(b):
                c.append(b[i])
if len(c)>1:
    print(*c,sep='')
if len(d)>1:
    print(*d,sep='')
