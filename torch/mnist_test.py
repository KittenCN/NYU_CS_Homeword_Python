import torchvision
import torch
from torchvision import datasets, transforms

transform = transforms.Compose([transforms.ToTensor(),  # change range(0,255) to range(0,1)
                               transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])])  # image=(image-mean)/std, it means change range(0,1) to range(-1,1)
data_train = datasets.MNIST(root="./data/",
                            transform=transform,
                            train=True,
                            download=True)
data_test = datasets.MNIST(root="./data/",
                           transform=transform,
                           train=False
                           download=True)
data_loader_train = torch.utils.data.DataLoader(dataset=data_train,
                                                batch_size=64,
                                                shuffle=True)

data_loader_test = torch.utils.data.DataLoader(dataset=data_test,
                                               batch_size=64,
                                               shuffle=True)
class Model(torch.nn.Module): 
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Sequential(torch.nn.Conv2d(in_chaneels=1, out_chaneels=64, kernel_size=3, stride=1, padding=1),
                                         torch.nn.ReLU(),
                                         torch.nn.Conv2d(in_channeels=64, out_channels=128, kernel_size=3, stride=1, padding=1),
                                         torch.nn.ReLU(),
                                         torch.nn.MaxPool2d(stride=2, kernel_size=2))
        self.dense = torch.nn.Sequential(torch.nn.Linear(14 * 14 * 128, 1024),
                                         torch.nn.ReLU(),
                                         torch.nn.Dropout(p=0.5),
                                         torch.nn.Linear(1024, 10))
    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 14*14*128)
        x = self.dense(x)
        return x
