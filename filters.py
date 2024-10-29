import numpy as np
a = int(input("Number of zeros"))
b = int(input("Number of poles"))
Zeroes = []
Poles = []
Hz = []
Hp = []
Hw = []
for i in range(a):
	z = complex(input("Zero location in the z-plane"))
	r = int(input("Zero location from the origin"))
	w = int(input("Frequency of the zero"))
	Zeroes.append(r*np.exp(1j*w))

for i in range(b):
	jp = complex(input("Pole location in the z-plane"))
	rp = int(input("pole location from the origin"))
	wp = int(input("Frequency of the pole"))
	Poles.append(rp*np.exp(1j*wp))	

W = np.arange(-np.pi, np.pi, 0.001*np.pi)
for i in range(len(Zeroes)):
	x = np.exp(-1j*i*W)
	Hz.append(1-x)
for i in range(len(Poles)):
	x =(np.exp(-1j*i*W))
	Hp.append(1/(1-x))
for a, b in zip(Hz, Hp):
	Hw.append(a*b)
print(abs(Hw))
