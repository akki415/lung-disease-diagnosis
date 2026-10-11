import torch.nn as nn
import torch.nn.functional as F 
import torch

class NeuralNetwork(nn.Module):   # NeuralNetwork class i.e (created by me) is inheriting from PyTorch's nn.Module(i.e base class for nn) class
    def __init__(self):           # constructor of your NeuralNetwork , runs auto when created

        super().__init__()    # job is to initialize the parent class (nn.Module).
        # So when you create your neural network, you need to initialize the nn.Module part too.
        # super(...) essentially says: "Run the initialization of my parent class."


 ## INPUT BLOCK 


        self.conv_block1 = nn.Sequential(
            nn.Conv2d(in_channels=3,       # since RGB
                    out_channels=8,        # Create 8 different filters that will learn 8 different types of features, gets deeper,
                                           # you can afford more feature channels because the spatial dimensions are becoming smaller using (pooling).
                    kernel_size=(3, 3), 
                    padding=0, 
                    bias=True),

            nn.ReLU(),
            nn.BatchNorm2d(8)       # performs batch normalization on the 8 feature channels produced by your convolution
        )
        self.poolingL1 = nn.MaxPool2d(2, 2)


 ## 1ST CONVOLUTION BLOCK         

        self.conv_block2 = nn.Sequential(
            nn.Conv2d(8, 20, 3, padding=0, bias=True),

            nn.ReLU(),
            nn.BatchNorm2d(20)
        )
        self.poolingL2 = nn.MaxPool2d(2, 2)


 ## 1ST CONVOLUTION BLOCK

        self.conv_block3 = nn.Sequential(
                    nn.Conv2d(20, 8, 3, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(8)
        )
        self.poolingL3 = nn.MaxPool2d(2, 2)


 # 3rd CONVOLUTION BLOCK

        self.conv_block4 = nn.Sequential(
                    nn.Conv2d(8, 20, 1, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(20)
        )
        

 # 4th CONVOLUTION BLOCK

        self.conv_block5 = nn.Sequential(
                    nn.Conv2d(20, 36, 3, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(36)
        )
                
 # 5th CONVOLUTION BLOCK

        self.conv_block6 = nn.Sequential(
                    nn.Conv2d(36, 20, 3, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(20)
        )
                

 # 6th CONVOLUTION BLOCK

        self.conv_block7 = nn.Sequential(
                    nn.Conv2d(20, 36, 1, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(36)
        )
                
 # 7ST CONVOLUTION BLOCK

        self.conv_block8 = nn.Sequential(
                    nn.Conv2d(36, 8, 3, padding=0, bias=True),
        
                    nn.ReLU(),
                    nn.BatchNorm2d(8)
        )

 # FULLY CONNECTED LAYERS
        # till here the format is => [batch, 8, H, W] but we need but, since we need 8 values not [format] for fcn
        self.gap = nn.AdaptiveAvgPool2d((1, 1)) # we use globalpooling => [batch, 8, 1, 1]
        #Each of the 8 channels has been reduced to one number — the average of all its H × W values.

        self.fc = nn.Sequential(
            nn.Linear(8, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 2),
        )

    def forward(self, x) -> float:
        x = self.conv_block1(x)
        x = self.poolingL1(x)

        x = self.conv_block2(x)
        x = self.poolingL2(x)

        x = self.conv_block3(x)
        x = self.poolingL3(x)

        x = self.conv_block4(x)
        x = self.conv_block5(x)
        x = self.conv_block6(x)
        x = self.conv_block7(x)
        x = self.conv_block8(x)

        x = self.gap(x)            # image = [batch, 8, 1, 1]
        x = torch.flatten(x, 1)    # image = [batch, 8]

        x = self.fc(x)

        return x

        
        