import requests
import json
import numpy as np
import torch
from torch.utils.data.dataset import TensorDataset
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import os
from tqdm import tqdm

days = ['0', '31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
months = ['0', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

in_data_ori = []
out_data_ori = []
pklfile = r'./model.pkl'

class fcnet(nn.Module):
    def __init__(self) -> None:
        super(fcnet, self).__init__()
        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, 64)
        self.fc4 = nn.Linear(64, 3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

for year in range(2015, 2016):
    pbar = tqdm(total=12, leave=True)
    for month in range(1, 13):
        pbar.update(1)
        url = "https://webapi.sporttery.cn/gateway/jc/football/getMatchResultV1.qry?matchPage=1&matchBeginDate=" + str(year) + "-" + months[month] + "-01&matchEndDate=" + str(year) + "-" + months[month] + "-" + days[month] + "&leagueId=&pageSize=999999&pageNo=1&isFix=0&pcOrWap=1"
        res = json.loads(requests.get(url).text)['value']['matchResult']
        for item in res:
            if item['a'] != '' and item['d'] != '' and item['h'] != '' and item['winFlag'] != '':
                # print(item['a'], item['d'], item['h'], item['winFlag'])
                in_data_ori.append([float(item['a']), float(item['d']), float(item['h'])]) # 1 * 3
                h = 0
                d = 0
                a = 0
                if str(item['winFlag']) == 'H':
                    h = 1
                elif str(item['winFlag']) == 'D':
                    d = 1
                elif str(item['winFlag']) == 'A':
                    a = 1
                out_data_ori.append([h, d, a]) # 1* 3
    pbar.close()
testnum = 100
train_in_data = in_data_ori[:len(in_data_ori) - testnum]
test_in_data = in_data_ori[len(in_data_ori) - testnum:]
train_out_data = out_data_ori[:len(out_data_ori) - testnum]
test_out_data = out_data_ori[len(out_data_ori) - testnum:]

train_in_data_tensor = torch.from_numpy(np.array(train_in_data)).float()
train_out_data_tensor = torch.from_numpy(np.array(train_out_data)).float()
test_in_data_tensor = torch.from_numpy(np.array(test_in_data)).float()
test_out_data_tensor = torch.from_numpy(np.array(test_out_data)).float()

train_dataset = TensorDataset(train_in_data_tensor, train_out_data_tensor)
test_dataset = TensorDataset(test_in_data_tensor, test_out_data_tensor)
train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=True)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = fcnet().to(device)
epochs = 100
lr = 1e-4

if os.path.exists(pklfile):
    net.load_state_dict(torch.load(pklfile))
    net.eval()
    print("load old model")

optimizer = torch.optim.Adam(net.parameters(), lr)
loss_func = nn.MSELoss().to(device)

for epoch in range(epochs):
    for inputs, targets in train_dataloader:
        inputs = inputs.to(device)
        targets = targets.to(device)
        outputs = net(inputs)
        loss = loss_func(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 1 == 0:
        print("epoch:", epoch + 1, "loss:", loss.item())
    if (epoch + 1) % 100 == 0:
        torch.save(net.state_dict(), pklfile)