import numpy as np
import matplotlib.pyplot as plt
def cyclic_delay(x, m):
    N = len(x)
    y = []
    
    for n in range(N):
        idx = (n - m) % N
        y.append(x[idx])
    
    return y

def circ_conv(x1, x2):
    z = []
    N = len(x1)
    a = x2[0]
    b = list(x2[1:])[::-1] 
    b.insert(0, a)          
    x2r = np.array(b)        
    # Perform the circular convolution
    for n in range(N):
        y = cyclic_delay(x2r, n)   
        z.append(np.dot(x1, y))   
    
    return z

def linear_conv_via_circular(x1, x2):
    N1 = len(x1)
    N2 = len(x2)
    N = N1 + N2 - 1
    x1_padded = np.pad(x1, (0, N - N1), 'constant')
    x2_padded = np.pad(x2, (0, N - N2), 'constant')
    
    result = circ_conv(x1_padded, x2_padded)
    
    return result

# Example usage
x1 = [1, 2, 0, 1]
x2 = [2, 2, 1, 1]

result = linear_conv_via_circular(x1, x2)
print("Linear Convolution via Circular Convolution:", result)
plt.stem(result)
plt.show()
