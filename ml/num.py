from tkinter import Y
from sympy import re
import torch
import numpy as np
from torch.autograd import Variable

Layer1 = torch.nn.Linear(in_features=10, out_features=5, bias=True)
inp = Variable(torch.randn(10, 1).view(-1, 10))
Layer1(inp)
print(Layer1.weight)
