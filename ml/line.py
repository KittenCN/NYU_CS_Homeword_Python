import torch
import torch.utils.data
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data.dataset import TensorDataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

use_gpu = torch.cuda.is_available()

def show_data(x_data = [1,2,3], y_data=[1,2,3]):
    plt.scatter(x_data, y_data, color='k')
    plt.show()

def show_data_cost(x_data = [1,2,3], y_data=[1,2,3], prediction_data=[1,2,3], loss=0, use_gpu=1):
    plt.cla()
    if use_gpu:
        x_data = x_data.cpu().detach().numpy()
        y_data = y_data.cpu().detach().numpy()
        prediction_data = prediction_data.cpu().detach().numpy()
        loss = loss.cpu().detach().numpy()
    else:
        x_data = x_data.detach().numpy()
        y_data = y_data.detach().numpy()
        prediction_data = prediction_data.detach().numpy()
        loss = loss.detach().numpy()
    
    plt.scatter(x_data, y_data, color='r')
    plt.scatter(x_data, prediction_data, color='b')
    plt.text(0,0, 'loss: %.5f' % loss, fontdict={'size': 20, 'color': 'red'})
    plt.pause(0.1)
    

class linear_net(nn.Module):
    def __init__(self) -> None:
        super(linear_net, self).__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(1, 10)
        self.fc3 = nn.Linear(20, 100)
        self.fc4 = nn.Linear(100, 50)
        self.fc5 = nn.Linear(50, 1)
    
    def forward(self, x):
        x1 = self.fc1(x)
        x2 = self.fc2(x)
        x3 = torch.cat((x1, x2), 1)
        x = self.fc3(x3)
        x = F.relu(x)
        x = self.fc4(x)
        x = F.relu(x)
        x = self.fc5(x)
        # x = F.dropout(0.5)
        return x

if __name__ == "__main__":
    # y = a * x + b
    a = 10
    b = 15
    c = 20
    x = torch.randn(1000).view(-1, 1)
    y = a * x * x + b * x + c
 
    dataset = TensorDataset(x, y)
    data_loader = DataLoader(dataset, batch_size = 32, shuffle = True)
    model = linear_net()
    optimizer = torch.optim.Adam(model.parameters(), lr = 1e-3)
    loss_func = nn.MSELoss()

    if(use_gpu):
        model = model.cuda()
        loss_func = loss_func.cuda()

    epochs = 500
    losses = []
    for epoch in range(epochs):
        for inputs, targets in data_loader:
            if(use_gpu):
                inputs = inputs.cuda()
                targets = targets.cuda()
            outputs = model(inputs)
            loss = loss_func(outputs, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        losses.append(loss.item())
        if(epoch % 10 == 0):
            print("Epoch: {}, Loss: {}".format(epoch, loss.item()))
            show_data_cost(inputs, outputs, targets, loss, use_gpu)
    
    print("Final Loss: {}".format(loss.item()))
    x_data = []
    for i in range(len(losses)):
        x_data.append(i)
    show_data(x_data, losses)