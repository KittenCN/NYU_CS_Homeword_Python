import torch
import numpy as np
from torch.autograd import Variable

def get_date():
    w = 10
    b = 15
    train_x = np.array(np.random.randn(50))
    train_y = np.array(w * train_x + b)
    x = Variable(torch.from_numpy(train_x).type(torch.FloatTensor), requires_grad=False).view(-1, 1)
    y = Variable(torch.from_numpy(train_y).type(torch.FloatTensor), requires_grad=False)
    return x, y

def get_weights():
    w = Variable(torch.FloatTensor([10]), requires_grad=True)
    b = Variable(torch.FloatTensor([15]), requires_grad=True)
    return w, b

def simple_network(x):
    y_pred = torch.matmul(x, w) + b
    return y_pred

def loss_func(y, y_pred):
    loss = (y_pred - y).pow(2).sum()
    for p in [w, b]:
        if not p.grad is None:
            p.grad.data.zero_()
    loss.backward()
    return loss.data

def optimize(lr):
    w.data = w.data - lr * w.grad.data
    b.data = b.data - lr * b.grad.data
    return

if __name__ == "__main__":
    x, y = get_date()
    w, b = get_weights()
    lr = 0.001
    for i in range(500):
        y_pred = simple_network(x)
        loss = loss_func(y, y_pred)
        optimize(lr)
        if i % 10 == 0:
            print(loss)