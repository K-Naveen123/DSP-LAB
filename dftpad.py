import numpy as np
from matplotlib import pyplot as plt
    
def dft(x,N):
    X=[]
    for k in np.arange(0,N):
        s=0
        for n in np.arange(0,N):
            s=s+x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    
    return np.array(X)
    
    

x1=[0,1,2,3,4,5,6,7,8,9,10]
X1=dft(x1,len(x1))
print(X1)
plt.figure(figsize=(10, 12))
plt.subplot(2,1,1)
plt.stem(np.arange(len(x1)),abs(X1))
plt.xlabel("Index")
plt.ylabel("X2")
plt.grid(True)


x2=[1,2,3,4,5,6,7,8,9,10]
x2=np.pad(x2,(0,10))
X2=dft(x2,len(x2))
print(X2)
plt.subplot(2,1,2)
plt.stem(np.arange(len(x2)),abs(X2))
plt.xlabel("Index")
plt.ylabel("X2")
plt.grid(True)
plt.show()
