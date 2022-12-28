import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#----------------------------------------
A=int(input("파동의 진폭을 입력하세요(cm):"))
T=int(input("파동의 주기를 입력하세요(s):"))
λ=int(input("파동의 파장을 입력하세요(cm):"))
#----------------------------------------
#변위 위치 그래프
a=A#진폭
b1=(2*np.pi)/λ#위치그래프 b
v1=λ/T
x1 = []
y1 = []
figure, ax = plt.subplots()
line1, = ax.plot(x1, y1)
plt.axis([0, 4*np.pi,-a-a/10,a+a/10])

def func_animate1(i):
    x1 = np.linspace(0, 4*np.pi, 100)
    y1 = a*np.sin(b1*x1 - v1/5 * i)
    
    line1.set_data(x1, y1)
    
    return line1,

plt.figure(1)
ani1 = FuncAnimation(figure,func_animate1,frames=1000,interval=50)
plt.ylabel("displacement")
plt.xlabel("distance")
#----------------------------------------
#변위 위치 그래프
a=A#진폭
b2=(2*np.pi)/T#위치그래프 b

figure, ax = plt.subplots()
x2 = np.linspace(0, 2*T,18*T)
y2 = a*np.sin(b2*x2)
plt.plot(x2,y2)

plt.figure(2)
plt.ylabel("displacement")
plt.xlabel("time")
#----------------------------------------
plt.show()
#----------------------------------------