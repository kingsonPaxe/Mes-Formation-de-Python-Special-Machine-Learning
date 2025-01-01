# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
print(x)

a = plt.axes(projection = "3d")
a.scatter(x[:,0], x[:,1], x[:,2], c = iris.target)
plt.show()