#导入库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from collections import Counter
import numpy as np

#导入iris数据集
iris = datasets.load_iris()
X = iris.data
Y = iris.target
X_train,x_test,Y_train,y_test = train_test_split(X,Y,random_state=2003)

#计算距离
def euc_dis(instance1, instance2):
    '''
    计算两个样本instance1和instance2之间的欧式距离
    instance1:第一个样本,array类型
    instance2:第二个样本,array类型
    '''
    dis = np.sqrt(np.sum((instance1 - instance2)**2))
    return dis

def knn_classify(X,Y,testInstance,k):
    '''
    给定一个测试数据testInstance,通过KNN算法来预测它的标签
    X:训练数据的特征
    Y:训练数据的标签
    testInstance:测试数据,假定一个测试数据array类型
    k:选择多少个neighbors
    '''
    #鸢尾花数据集提供了三种鸢尾花
    #返回testInstance的预测标签 = {0,1,2}

    #计算testInstance与X的距离
    dists = [euc_dis(testInstance,X) for x in X]

    #找出最近的K个元素的idx
    idxknn = np.argsort(dists)[:k]#将dists从小到大排序，返回排序后元素indices

    #找出KNN对应的n个y值
    yknn = Y[idxknn]

    #返回结果
    return Counter(yknn).most_common(1)[0][0]

#预测结果
predictions = [knn_classify(X_train,Y_train,data,3) for data in x_test]
accuracy = np.count_nonzero((predictions==y_test)==True)
print("Accuracy is: %.3f" %(accuracy/len(x_test)))
