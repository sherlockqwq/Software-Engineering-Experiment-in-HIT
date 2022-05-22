import csv
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
csv_reader = csv.reader(open("E:/Download/QQDownload/2201110126/2201110126/data/data1_x.csv"))
for line in csv_reader:
  x.append([1.0, float(line[0])])
csv_reader = csv.reader(open("E:/Download/QQDownload/2201110126/2201110126/data/data1_y.csv"))
for line in csv_reader:
  y.append([float(line[0])])
x = np.array(x)
y = np.array(y)

# 判断达到收敛条件
eps = 1e-8
def judge(nextTheta: np.ndarray, theta: np.ndarray):
  return np.linalg.norm(nextTheta - theta) ** 2 < eps

# 迭代公式
alpha = 0.01
def getNextTheta(theta: np.ndarray):
  nextTheta = theta - alpha / len(x) * np.dot(x.T, (np.dot(x, theta) - y))
  return nextTheta

# 迭代过程
theta = np.array([[0.0], [0.0]])
nextTheta = getNextTheta(theta)
# historyTheta记录迭代过程中的theta用于绘图
historyTheta = []
while not judge(nextTheta, theta):
  historyTheta.append(theta.copy())
  theta = nextTheta.copy()
  nextTheta = getNextTheta(theta)

def h(theta: np.ndarray, x: np.ndarray):
  return np.dot(x, theta)

# 预测
print(theta)
print("对3.5的预测结果为：", h(theta, np.array([1.0, 3.5])))
print("对7.0的预测结果为：", h(theta, np.array([1.0, 7.0])))


def J(theta: np.ndarray):
  return (np.linalg.norm(h(theta, x) - y) ** 2) * len(x) / 2

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