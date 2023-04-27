import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

arr = [4,8,6,7,8,9,9,8,7,6,5]

plt.plot(arr)
plt.ylabel("Numeros")
plt.show()

plt.figure()
x1 = [3,2,4,1]
x2 = [1,3,16,9]
plt.plot(x1, x2)
plt.show()

plt.figure()
plt.plot(x1,x2,'ro')
plt.axis([0,20,0,10])
plt.grid()
plt.show()

plt.figure()
t = np.arange(-5,5, .2)
plt.plot(t,t,'r--', t, t**2, 'bs', t, t**3, 'go')

plt.show()

grupos = ['grupo 1', 'grupo 2', 'grupo 3']
valores = [1, 10, 100]
plt.figure()
plt.subplot(1,3,1)
plt.bar(grupos, valores)
plt.subplot(1,3,2)
plt.scatter(grupos, valores)
plt.subplot(1,3,3)
plt.plot(grupos,valores)
plt.suptitle("Tipos de graficas")
plt.show()

def f(x):
    y = 6 * x ** 3 + 5
    return y

def fPrima(x):
    y = 18 * x ** 2 
    return y

def fPrima2(x):
    y = 36 * x
    return y


t=np.arange(-5,5,0.001)
plt.figure()

plt.subplot(1,3,1)
plt.title("f(x)")
plt.plot(t,f(t),"g")

plt.subplot(1,3,2)
plt.title("f´(x)")
plt.plot(t,fPrima(t),"b")

plt.subplot(1,3,3)
plt.title("f´´(x)")
plt.plot(t,fPrima2(t),"y")
plt.suptitle("funciones derivadas")
plt.show()

t=np.arange(0,50,0.0001)
plt.figure()
plt.plot(t,f(t),'k',t,fPrima(t),'bo')
plt.show()




# img=mpimg.imread('"joker-1.jpg"')
# height,width,channels=img.shape
# imgGray=np.zeros((height,width))
# for i in range(height):
#     for j in range(width):
#         imgGray[i,j]=(int(img[i,j,0])\
#             +int(img[i,j,1])+int(img[i,j,2]))//3
# plt.figure()
# plt.imshow(img)
# plt.figure()
# plt.imshow(imgGray,cmap=plt.cm.inferno)