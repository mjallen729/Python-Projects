import numpy as np
import torch
import torchvision
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import nn, optim

# ToTensor() converts the image into numbers between 0 and 255
# These values are then scaled to a range between 0 and 1
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,))])

pathname = '/Users/matt/Documents/DataSets/MNIST'

trainset = datasets.MNIST(pathname, download= True, train= True, 
                            transform= transform)

valset = datasets.MNIST(pathname, download= True, train= False,
                            transform= transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size= 64,
                                            shuffle= True)

valloader = torch.utils.data.DataLoader(valset, batch_size= 64,
                                            shuffle= True)

def visualization():
    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    print(images.shape)
    print(labels.shape)

    figure = plt.figure()
    num_images = 60
    for i in range(1, num_images + 1):
        plt.subplot(6, 10, i)
        plt.axis('off')
        plt.imshow(images[i].numpy().squeeze(), cmap= 'gray_r')
    
    plt.show()

visualization()


input_size = 784
hidden_sizes = [128, 64]
output_size = 10

model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                        nn.ReLU(),
                        nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                        nn.ReLU(),
                        nn.Linear(hidden_sizes[1], output_size),
                        nn.LogSoftmax(dim= 1))

criterion = nn.NLLLoss()
images, labels = next(iter(trainloader))
images = images.view(images.shape[0], -1)

logps = model(images)  # log probabilities
loss = criterion(logps, labels)  # Calculate NLL loss

optimizer = optim.SGD(model.parameters(), lr= 0.003, momentum= 0.9)
time0 = time()

epochs = 15
for e in range(epochs):
    running_loss = 0

    for images, labels in trainloader:
        # Flatten images into input
        images = images.view(images.shape[0], -1)

        # Training pass
        optimizer.zero_grad()

        output = model(images)
        loss = criterion(output, labels)

        # Model learns by backpropagating
        loss.backward()

        # Optimizes weights
        optimizer.step()

        running_loss += loss.item()

    else:
        print('Epoch {} - Training loss: {}'.format(e,
                                            running_loss / len(trainloader)))

print('\nTraining Time (in minutes) =', (time() - time0) / 60)

def validate():
    def view_classify(img, ps):
        ''' 
        Function for viewing an image and it's predicted classes.

        '''
        ps = ps.data.numpy().squeeze()

        fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
        ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
        ax1.axis('off')
        ax2.barh(np.arange(10), ps)
        ax2.set_aspect(0.1)
        ax2.set_yticks(np.arange(10))
        ax2.set_yticklabels(np.arange(10))
        ax2.set_title('Class Probability')
        ax2.set_xlim(0, 1.1)
        plt.tight_layout()
        plt.show()

    images, labels = next(iter(valloader))

    img = images[0].view(1, 784)
    with torch.no_grad():
        logps = model(img)

    ps = torch.exp(logps)
    probab = list(ps.numpy()[0])
    print("Predicted Digit =", probab.index(max(probab)))
    view_classify(img.view(1, 28, 28), ps)

validate()


correct_count, all_count = 0, 0
for images,labels in valloader:
  for i in range(len(labels)):
    img = images[i].view(1, 784)
    with torch.no_grad():
        logps = model(img)

    
    ps = torch.exp(logps)
    probab = list(ps.numpy()[0])
    pred_label = probab.index(max(probab))
    true_label = labels.numpy()[i]
    if(true_label == pred_label):
      correct_count += 1
    all_count += 1

print("Number Of Images Tested =", all_count)
print("\nModel Accuracy =", (correct_count/all_count))

torch.save(model, './model.pt')