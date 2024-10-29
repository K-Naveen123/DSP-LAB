def circular_convolution(x, h):
    N = len(x)
    result = np.zeros(N)
    
    for n in range(N):
        for m in range(N):
            result[n] += int(x[m] * h[(n - m) % N])
    
    return result

import numpy as np

x = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
h = [1, -1, 1]
m=len(h)
N = len(x)
l = 4
#int(input("Enter L Value: "))
k = [x[i:i + l] for i in range(0, len(x), l)]
# print(k)
for i in range(len(h) - 1):
    for j in range(len(k)):
        k[j].append(0)
# print(k)
for i in range(l-1):
    h.append(0)

y = []
for i in range(len(k)):
    y.append(list(circular_convolution(k[i], h)))
print("After Convolution: ",y)
result = y[0]
for i in range(1, len(y)):
        ov_l = m-1
        for j in range(ov_l):
            result[-(ov_l - j)] += y[i][j]
        result.extend(y[i][ov_l:])
    

print("Final Output: ",result[:-2])
