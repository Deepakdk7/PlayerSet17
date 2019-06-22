ax=list(input())
for i in range(0,len(ax)):
    if ord(ax[i])>48 and ord(ax[i])<57:
        print(ax[i-1]*int(ax[i]),end='')
