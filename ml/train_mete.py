import numpy as np
import glob
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import math

def RP(t, h):
    # γ = 常数a与大气温度T的乘积 与 常数b与大气温度T的和 的商 与 大气湿度RH与100的商的自然对数 的和
    # 露点温度 = 常数b与函数γ的乘积 与 常数a与函数γ的差 的 商
    a = 17.27
    b = 237.7
    y = ((a * t) / (b + t)) + math.log(h / 100)
    Td = (b * y) / (a - y)
    return Td

list_pre = []
list_tem = []
list_rhu = []
list_prs = []

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

txt_list = glob.glob('D:\\workstation\\GitHub\\NYU_CS_Homework_Python\\ml\\Meteorological forecast\\data\\TXT\\*.txt')
bar = tqdm(total=len(txt_list))
for txt_file in txt_list:
    # print(txt_file, len(txt_file), txt_file[-20:-17])
    bar.update(1)
    with open(txt_file, 'r') as f:
        data = f.readlines()
        for line in data:
            sp = line.split()
            if txt_file[-20:-17] == 'PRE':
                if sp[9] == '0':
                    list_pre.append(0)
                else:
                    list_pre.append(1)
            if txt_file[-20:-17] == 'TEM':
                list_tem.append(int(sp[7]))
            if txt_file[-20:-17] == 'RHU':
                list_rhu.append(int(sp[7]))
            if txt_file[-20:-17] == 'PRS':
                list_prs.append(int(sp[7]))
bar.close()

print(len(list_pre), len(list_tem), len(list_rhu), len(list_prs))

pre_list_train = []
pre_list_test = []
rainfall_train = []
rainfall_test = []

index = 0
# maxnum = len(list_pre)
maxnum = 1000
while index < maxnum:
    if index <= maxnum * 0.8:
        temp = [RP(list_tem[index] / 10, list_rhu[index])]
        pre_list_train.append(temp)
        rainfall_train.append(list_pre[index])
    else:
        temp = [RP(list_tem[index] / 10, list_rhu[index])]
        pre_list_test.append(temp)
        rainfall_test.append(list_pre[index])
    index += 1

pre_al_train = np.array(pre_list_train)
pre_al_test = np.array(pre_list_test)
rainfall_al_train = np.array(rainfall_train)
rainfall_al_test = np.array(rainfall_test)

pre_train = torch.from_numpy(pre_al_train).float()
pre_test = torch.from_numpy(pre_al_test).float()
rainfall_train = torch.from_numpy(rainfall_al_train).float()
rainfall_test = torch.from_numpy(rainfall_al_test).float()

print(pre_train.size(), rainfall_train.size())

train_dataset = torch.utils.data.TensorDataset(pre_train, rainfall_train)
test_dataset = torch.utils.data.TensorDataset(pre_test, rainfall_test)

class weather(nn.Module):
    def __init__(self):
        super(weather, self).__init__()
        self.fc1 = nn.Linear(1, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, 64)
        self.fc4 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

if __name__ == "__main__":
    net = weather().to(device)
    loss_fn = nn.MSELoss().to(device)
    optimizer = optim.Adam(net.parameters(), lr=0.0001)
    for epoch in range(50):
        for inputs, targets in train_dataset:
            inputs = inputs.to(device)
            targets = targets.to(device)
            outputs = net(inputs)
            optimizer.zero_grad()
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()
        if epoch % 10 == 0:
            print(epoch, loss.item())
    
    for inputs, targets in test_dataset:
        inputs = inputs.to(device)
        targets = targets.to(device)
        outputs = net(inputs)
        loss = loss_fn(outputs, targets)
    print(loss.item())