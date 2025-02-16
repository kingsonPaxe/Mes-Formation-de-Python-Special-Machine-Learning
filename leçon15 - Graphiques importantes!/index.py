import matplotlib.pyplot as plt
import numpy as np
# f = lambda x,y: np.sin(x)*y + np.cos(y) *x
# x = np.linspace(-3, 5, 50)
# y = np.linspace(-3,5,50)

# X,Y = np.meshgrid(x,y)
# axes = plt.axes(projection = "3d")
# z = f(X,Y)
# axes.plot_surface(X,Y,z, cmap = "plasma")

# print(f"x data: {x}\n e de dimensao {x.ndim}")
# print(f"y data: {y}\n e de dimensao {y.ndim}")


# print(f"X data: {X}\n e de dimensao {X.ndim}")
# print(f"Y data: {Y}\n e de dimensao {Y.ndim}")

# plt.title("En utilizand la function meshgrid")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


# x = np.linspace(0,5,100)
# y = np.linspace(0,5,100)
# print(f"x_menor = {x}\n")
# print(f"y_menor = {y}\n")

# X, Y= np.meshgrid(x,y)
# print(f"X = {X}\n e tem um tamanho de {X.shape}")
# print(f"Y = {Y}\n e tem um tamanho de {X.shape}")

# f = lambda x, y: np.sin(x) + np.cos(x+y)
# z = f(X,Y)

# print(f"Z = {z}\n")
# axes = plt.axes(projection = "3d")
# axes.plot_surface(X,Y,z, cmap = "plasma")
# plt.title("En utilisant la function meshgrid ")
# plt.contour(X,Y,z)
# plt.colorbar()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data # Onde esta os dados
y = iris.target # Classe ou tipo de flores
names = list(iris.target_names)

ax = plt.axes(projection='3d')
ax.scatter(x[:,0], x[:,1], x[:,2], c = y)

plt.ylabel('y')
plt.xlabel('x')
handle = [plt.Line2D([0],[0], marker = "o", label = name, markerfacecolor=plt.cm.viridis((i/2)), color="w", markersize=8) for i, name in enumerate(names)]
plt.legend(handles = handle)
plt.show()