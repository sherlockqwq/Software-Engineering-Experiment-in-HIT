import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
csv_reader = csv.reader(open("E:/Download/QQDownload/2201110126/2201110126/data/data2_x.csv"))
for line in csv_reader:
  x.append([1.0, float(line[0].split("   ")[1]), float(line[0].split("   ")[2])])
csv_reader = csv.reader(open("E:/Download/QQDownload/2201110126/2201110126/data/data2_y.csv"))
for line in csv_reader:
  y.append([float(line[0])])

# 标准化
x = np.array(x)
y = np.array(y)
sigma = [np.std(x[:, i]) for i in range(3)]
mu = [np.mean(x[:, i]) for i in range(3)]
x[:, 1] = (x[:, 1] - mu[1]) / sigma[1]
x[:, 2] = (x[:, 2] - mu[2]) / sigma[2]

def J(theta: np.ndarray):
  return (np.linalg.norm(np.dot(x, theta) - y) ** 2) / (len(x) * 2)

# 计算梯度
def getGradient(theta: np.ndarray):
  return np.dot(x.T, (np.dot(x, theta) - y)) / len(x)

# 黄金分割求步长
eps = 1e-6
def getAlpha(theta: np.ndarray, d: np.ndarray):
  l = 0.001
  r = 10
  while (r - l > eps):
    ll = l + (r - l) * 0.382
    rr = l + (r - l) * 0.618
    if (J(theta + ll * d) < J(theta + rr * d)):
      r = rr
    else:
      l = ll
  return l

# 迭代过程
historyTheta = []
theta = np.array([[0.0], [0.0], [0.0]])
d = -getGradient(theta)
alpha = getAlpha(theta, d)
while np.linalg.norm(d) > eps:
  theta = theta + alpha * d
  d = -getGradient(theta)
  alpha = getAlpha(theta, d)
  historyTheta.append(theta.copy())

# 预测
print(theta)
print("对题目要求的预测为",np.dot(np.array([1.0, (1650.0 - mu[1]) / sigma[1], (3.0 - mu[2]) / sigma[2]]), theta))

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('迭代次数')
plt.ylabel('h_θ (x)')
x_data = []
y_data = []
for i in range(len(historyTheta)):
  x_data.append(i)
  y_data.append(J(historyTheta[i]))
plt.plot(x_data, y_data)
plt.show()