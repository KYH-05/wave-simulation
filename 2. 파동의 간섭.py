import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#----------------------------------------
A1=int(input("첫번째 파동의 진폭을 입력하세요(cm):"))
T1=int(input("첫번째 파동의 주기를 입력하세요(s):"))
λ1=int(input("첫번째 파동의 파장을 입력하세요(cm):"))
A2=int(input("두번째 파동의 진폭을 입력하세요(cm):"))
T2=int(input("두번째 파동의 주기를 입력하세요(s):"))
λ2=int(input("두번째 파동의 파장을 입력하세요(cm):"))
K=int(input("위상이 같으면 1을 위상이 다르면 -1을 입력하세요"))
S=int(input("두 파동 사이의 거리를 입력하세요(cm):"))
#----------------------------------------
#변위 위치 그래프
x=[]
y=[]
a1=A1#진폭
b1=(2*np.pi)/λ1#위치그래프 b
v1=λ1/T1
x1 = []
y1 = []
figure, ax = plt.subplots()
line, = ax.plot(x, y)
#----------------------------------------
#변위 위치 그래프
a2=A2#진폭
b2=(2*np.pi)/λ2#위치그래프 b
v2=λ2/T2
x2 = []
y2 = []
#----------------------------------------
def init():
    return line,
#----------------------------------------
def func_animate2(i):
    y1=[]
    y2=[]
    x1 = np.linspace(-S,2*S,100*S)
    x2 = np.linspace(-S,2*S,100*S)
    #---------------------------------------------------------
    for k in range(len(x1)):
      if -S+0.1*i<=x1[k]<=0+0.1*i:
        SI=a1*np.sin(b1*x1[k]-v1/8*i)
        y1=np.append(y1,np.array([np.round(SI,3)]))
      else:
        y1=np.append(y1,np.array([np.round(0,3)]))
    #---------------------------------------------------------
    for k in range(len(x2)):
      if S-0.1*i<=x2[k]<=2*S-0.1*i:
        SI2=K*a2*np.sin(b2*x2[k]- v2/8 * i)
        y2=np.append(y2,np.array([np.round(SI2,3)]))
      else:
        y2=np.append(y2,np.array([np.round(0,3)]))
      
    #---------------------------------------------------------
    x = np.linspace(-S,2*S,100*S)
    y=y1+y2
    line.set_data(x,y)
    return line,
ani2 = FuncAnimation(figure,func_animate2,init_func=init,frames=1000,interval=50)
#----------------------------------------
plt.axis([0, S,-a1-a2,a1+a2])
plt.figure(1)
plt.ylabel("displacement")
plt.xlabel("distance")
plt.show()
#----------------------------------------