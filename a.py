import torch
import torch.nn as nn
class Net(nn.Module):
    def __init__(self, input_size, hidden_size, output_size) -> None:
        super().__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.sigmoid=torch.nn.Sigmoid()
        self.fc2=nn.Linear(hidden_size,output_size)
    def forward(self,x,w1,w2):
        self.fc1.weight.data=w1
        self.fc1.bias.data=torch.Tensor([0])
        out=self.fc1(x)
        out=self.sigmoid(out)

        self.fc2.weight.data = w2
        self.fc2.bias.data = torch.Tensor([0])
        output = self.fc2(out)
        output = self.sigmoid(output)
        return output
if __name__=='__main__':
    x=torch.tensor([0.5,0.3])
    y=torch.tensor([0.23,0.07])
    w1=torch.tensor([[0.2,0.5],[-0.4,0.6]])
    w2=torch.tensor([[0.1,-0.3],[-0.5,0.8]])
    net=Net(2,2,2)

    loss=nn.MSELoss()
    optimizer=torch.optim.SGD(params=net.parameters(),lr=1e-2)

    for i in range(1000):
        output=net(x,w1,w2)
        loss_fn=loss(output,y)
        optimizer.zero_grad()
        loss_fn.backward()
        optimizer.step()
        print("损失函数的变化情况",i,loss_fn)
    print(output)