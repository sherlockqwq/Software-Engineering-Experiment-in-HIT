import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
csv_reader = csv.reader(open(r"E:/Download/QQDownload/2201110126/2201110126/data/data2x.csv"))
for line in csv_reader:
  x.append([1.0, float(line[0].split("   ")[1]), float(line[0].split("   ")[2])])
csv_reader = csv.reader(open("E:/Download/QQDownload/2201110126/2201110126/data/data2y.csv"))
for line in csv_reader:
  y.append([float(line[0])])
x = np.array(x)
y = np.array(y)

def h(x: np.ndarray, theta: np.ndarray):
  return 1 / (1 + np.exp(-np.dot(x, theta)))

# 计算梯度
def getGradient(theta: np.ndarray):
  return np.dot(x.T, (h(x, theta) - y)) / len(x)

# 计算海塞矩阵
def getHessian(theta: np.ndarray):
  # print((h(x, theta) * (1 - h(x, theta))).reshape(-1).shape)
  # print(np.diag((h(x, theta) * (1 - h(x, theta))).reshape(-1)).shape)
  return np.dot(np.dot(x.T, np.diag((h(x, theta) * (1 - h(x, theta))).reshape(-1))), x) / len(x)

def L(theta: np.ndarray):
  return (np.linalg.norm(np.dot(y.T, np.log(h(x, theta)))) + np.linalg.norm(np.dot((1 - y).T, np.log(1 - h(x, theta))))) / len(x)

def getNextTheta(theta: np.ndarray):
  return theta - np.dot(np.linalg.inv(getHessian(theta)), getGradient(theta))

# 迭代过程
eps = 1e-6
historyTheta = []
theta = np.array([[0.0], [0.0], [0.0]])
nextTheta = getNextTheta(theta)
while np.linalg.norm(nextTheta - theta) ** 2 >= eps:
  theta = nextTheta
  nextTheta = getNextTheta(theta)
  historyTheta.append(theta.copy())

# 预测
print(theta)
print("预测能否录取",h(np.array([1.0, 20.0, 80.0]), theta))
print("能录取" if h(np.array([1.0, 20.0, 80.0]), theta) > 0.5 else "不行")

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('迭代次数')
plt.ylabel('L_θ (x)')
x_data = []
y_data = []
for i in range(len(historyTheta)):
  x_data.append(i)
  y_data.append(L(historyTheta[i]))
plt.plot(x_data, y_data)
plt.show()