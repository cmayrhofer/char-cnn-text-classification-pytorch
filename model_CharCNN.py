import torch
import torch.nn as nn
import torch.nn.functional as F


class  CharCNN(nn.Module):
    
    def __init__(self, args):
        super(CharCNN, self).__init__()
        
        self.num_features = args.num_features
        self.conv1 = nn.Sequential(
            nn.Conv1d(self.num_features, 256, kernel_size=7, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.conv2 = nn.Conv1d(256, 256, kernel_size=7, stride=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool1d(kernel_size=3, stride=3)
            
            
        self.conv3 = nn.Conv1d(256, 256, kernel_size=3, stride=1)
        self.relu3 = nn.ReLU()
        
        self.conv4 = nn.Conv1d(256, 256, kernel_size=3, stride=1)
        self.relu4= nn.ReLU()    
            
        
        self.conv5 = nn.Conv1d(256, 256, kernel_size=3, stride=1)
        self.relu5= nn.ReLU()
        
        self.conv6 = nn.Conv1d(256, 256, kernel_size=3, stride=1)
        self.relu6= nn.ReLU()
        self.pool6 = nn.MaxPool1d(kernel_size=3, stride=3)
        
            
        
        self.fc1 = nn.Linear(8704, 1024)
        self.relu7= nn.ReLU()
        self.dropout7= nn.Dropout(p=args.dropout)
            
        
        self.fc2 = nn.Linear(1024, 1024)
        self.relu8= nn.ReLU()
        self.dropout8= nn.Dropout(p=args.dropout)
            
        
        self.fc3 = nn.Linear(1024, 4)
        self.softmax = nn.LogSoftmax()
        # self.inference_log_softmax = InferenceBatchLogSoftmax()

    def forward(self, x):
        x = self.conv1(x)
        # print('x.size()', x.size())
        # x = self.relu1(x)
        # print('x.size()', x.size())
        # x = self.pool1(x)
        # print('x.size()', x.size())
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        # print('x.size()', x.size())
        x = self.conv3(x)
        x = self.relu3(x)
        x = self.conv4(x)
        x = self.relu4(x)
        x = self.conv5(x)
        x = self.relu5(x)
        x = self.conv6(x)
        x = self.relu6(x)
        x = self.pool6(x)

        x = x.view(x.size(0), -1)
       
        x = self.fc1(x)
        x = self.relu7(x)
        x = self.dropout7(x)
       
        x = self.fc2(x)
        x = self.relu8(x)
        x = self.dropout8(x)
       
        x = self.fc3(x)
       

        x = self.softmax(x)

        return x