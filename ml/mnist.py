import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 处理数据
train_dataset = datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

class ResBlock(nn.Module):
    def __init__(self, in_place, out_place, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=in_place, out_channels=out_place, kernel_size=3, padding=1, stride=stride)
        self.bn1 = nn.BatchNorm2d(out_place)
        self.conv2 = nn.Conv2d(in_channels=out_place, out_channels=out_place, kernel_size=3, padding=1, stride=1)
        self.bn2 = nn.BatchNorm2d(out_place)
        self.shortcut = nn.Sequential()
        if stride != 1 or in_place != out_place:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels=in_place, out_channels=out_place, kernel_size=1, stride=stride),
                nn.BatchNorm2d(out_place)
            )
    
    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = F.relu(out)
        return out

class ResNet18(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.layer1 = self.make_layer(in_place=64, out_place=64, block_num=2, stride=1)
        self.layer2 = self.make_layer(in_place=64, out_place=128, block_num=2, stride=2)
        self.layer3 = self.make_layer(in_place=128, out_place=256, block_num=2, stride=2)
        self.layer4 = self.make_layer(in_place=256, out_place=512, block_num=2, stride=2)
        self.fc = nn.Linear(512, 10)
    
    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = F.avg_pool2d(out, 4)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out
    
    def make_layer(self, in_place, out_place, block_num, stride):
        layers = []
        layers.append(ResBlock(in_place, out_place, stride))
        for i in range(1, block_num):
            layers.append(ResBlock(out_place, out_place))
        return nn.Sequential(*layers)

class LeNet5(nn.Module):
    def __init__(self) -> None:
        super(LeNet5, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)  
        self.conv2 = nn.Conv2d(6, 16, 5) 
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = x.view(x.size()[0], -1) 
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class mnist_net(nn.Module):
    def __init__(self):
        super(mnist_net, self).__init__()
        # conv = (inputsize + 2 * padding - kernal_size) / stride + 1
        # maxpool = (inputsize - kernal_size) / stride + 1 
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, padding = 1)  
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding = 1) 
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2) 
        self.fc1 = nn.Linear(in_features=14*14*128, out_features=1024)  
        self.fc2 = nn.Linear(in_features=1024, out_features=512)  
        self.fc3 = nn.Linear(in_features=512, out_features=10) 
        self.drop1 = nn.Dropout(p=0.5)
    
    def forward(self, x):
        x = F.relu(self.conv1(x)) # 28*28*1 -> 28*28*64
        x = F.relu(self.conv2(x)) # 28*28*64 -> 28*28*128
        x = self.pool1(x) # 28*28*128 -> 14*14*128
        x = x.view(-1, 14*14*128)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.drop1(x)
        x = self.fc3(x)
        return x

net = ResNet18().to(device)
print(net)
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
epochs = 1

for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        outputs = net(images)
        loss_ = loss(outputs, labels)
        optimizer.zero_grad()
        loss_.backward()
        optimizer.step()
        if (i+1) % 10 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                  .format(epoch+1, epochs, i+1, len(train_loader), loss_.item()))

torch.save(net, 'mnist_cnn.pth') # 保存模型
net = torch.load('mnist_cnn.pth') # 加载模型
print("---------------------------------------------")
print(net)
correct = 0
for data in test_loader:
    images, labels = data
    images = images.to(device)
    labels = labels.to(device)
    outputs = net(images)
    _, predicted = torch.max(outputs.data, 1)
    correct += (predicted == labels).sum().item()
print('Accuracy of the network: {} %'.format(correct / len(test_loader)))


