import numpy as np

"""
函数说明:创建数据集

Parameters:
    无
Returns:
    group - 数据集
    labels - 分类标签
Modify:
    2017-07-13
"""
def createDataSet():
    #四组二维特征
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组特征的标签
    labels = ['爱情片','爱情片','动作片','动作片']
    return group, labels
if __name__ == '__main__':
    #创建数据集
    group, labels = createDataSet()
    #打印数据集
    print(group)
    print(labels)