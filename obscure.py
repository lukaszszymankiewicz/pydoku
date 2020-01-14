import numpy as np
ps = np.mgrid[1:10,1:10,1:10][2]
def solve(s):
    global ps
    i,n,ps[i[0],i[1],:],ps[:,i[1],n],ps[i[0],:,n]=np.nonzero(s),s[np.nonzero(s)]-1,0,0,0
    for ax in [2,1,0]:s |= np.where((ps!=0).sum(ax,keepdims=True)>1,0,ps).sum(2)
    for b,r,c in zip(n,i[0]//3*3,i[1]//3*3): ps[np.ix_(np.arange(r,r+3),np.arange(c,c+3), [b])]=0
    return solve(s) if 0 in s else s