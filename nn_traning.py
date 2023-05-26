import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

def relu(t):
    return np.maximum(t,0)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def sparse_cross_entropy(z,y):
    return -np.log(z[0,y])

def to_full(y, num_classes):
    y_full = np.zeros((1, num_classes))
    y_full[0,y] = 1
    return y_full

def relu_deriv(t):
    return (t >= 0).astype(float)

def predict(x):
    t1 = x @ w1 + b1
    h1 = relu(t1)
    t2 = h1 @ w2 + b2
    z = softmax(t2)
    return z

def calc_accuracy():
    correct = 0
    for x, y in dataset:
        z = predict(x)
        y_pred = np.argmax(z)
        if y_pred == y:
            correct += 1
    acc = correct / len(dataset)
    return acc


INPUT_DIM = 4 #Количество входных значений
OUT_DIM = 3 #Количество выходных значений (количество классов)
H_DIM = 10 #Количество нейронов в первом слое сети

TRANING_SPEED = 0.001
NUM_EPOCHS = 400

iris = datasets.load_iris()
dataset = [(iris.data[i][None, ...],iris.target[i]) for i in range(len(iris.target))]


w1 = np.random.randn(INPUT_DIM,H_DIM)
b1 = np.random.randn(1,H_DIM)
w2 = np.random.randn(H_DIM,OUT_DIM)
b2 = np.random.randn(1,OUT_DIM)

"""w1 = (w1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
b1 = (b1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
w2 = (w2 - 0.5) * 2 * np.sqrt(1/H_DIM)
b2 = (b2 - 0.5) * 2 * np.sqrt(1/H_DIM)"""

loss_arr = []

for ep in range(NUM_EPOCHS):
    random.shuffle(dataset)
    for i in range(len(dataset)):

        x,y = dataset[i]

        #FORWARD
        t1 = x @ w1 + b1
        h1 = relu(t1)
        t2 = h1 @ w2 + b2
        z = softmax(t2)
        e = sparse_cross_entropy(z, y)

        #BACKWARD
        y_full = to_full(y, OUT_DIM)
        dE_dt2 = z - y_full
        dE_dW2 = h1.T @ dE_dt2
        dE_db2 = dE_dt2
        dE_dh1 = dE_dt2 @ w2.T
        dE_dt1 = dE_dh1 * relu_deriv(t1)
        dE_dW1 = x.T @ dE_dt1
        dE_db1 = dE_dt1

        #UPDATE
        w1 = w1 - TRANING_SPEED * dE_dW1
        b1 = b1 - TRANING_SPEED * dE_db1
        w2 = w2 - TRANING_SPEED * dE_dW2
        b2 = b2 - TRANING_SPEED * dE_db2

        loss_arr.append(e)

accuracy = calc_accuracy()
print("Точность определения: ", accuracy)

plt.plot(loss_arr)
plt.show()
