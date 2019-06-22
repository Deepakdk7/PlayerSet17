def A(ax):
    for i in range(0,ax):
        if 2**i==ax:
            print(ax)
            break
    else:
        ax=ax+1
        A(ax)
ax=int(input(),2)
A(ax)
