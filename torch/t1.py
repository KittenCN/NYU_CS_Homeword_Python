import torch
x = torch.rand(4, 4)
y = x.view(16)
z = x.view(-1, 2)
print(x.size(), y.size(), z.size())