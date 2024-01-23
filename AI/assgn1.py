
#Import
import numpy as np
import matplotlib.pyplot as plt
import torch

# Preparing a toy dataset
data = np.genfromtxt('perceptron_toydata.txt', delimiter='\t')
X, y = data[:, :2], data[:, 2]
y = y.astype(np.int)

print('Class label counts:', np.bincount(y))
print('X.shape:', X.shape)
print('y.shape:', y.shape)

# Shuffling & train/test split
shuffle_idx = np.arange(y.shape[0])
shuffle_rng = np.random.RandomState(123)
shuffle_rng.shuffle(shuffle_idx)
X, y = X[shuffle_idx], y[shuffle_idx]

X_train, X_test = X[shuffle_idx[:70]], X[shuffle_idx[70:]]
y_train, y_test = y[shuffle_idx[:70]], y[shuffle_idx[70:]]

# Normalize (mean zero, unit variance)
mu, sigma = X_train.mean(axis=0), X_train.std(axis=0)
X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma

plt.scatter(X_train[y_train==0, 0], X_train[y_train==0, 1], label='class 0', marker='o')
plt.scatter(X_train[y_train==1, 0], X_train[y_train==1, 1], label='cl ass 1', marker='s')
plt.title('Training set')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.xlim([3, 3])
plt.ylim([3, 3])
plt.legend()

plt.show()
plt.scatter(X_test[y_test==0, 0], X_test[y_test==0, 1], label='class 0', marker='o')
plt.scatter(X_test[y_test==1, 0], X_test[y_test==1, 1], label='class 1', marker='s')
plt.title('Test set')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.xlim([3, 3])
plt.ylim([3, 3])
plt.legend()
plt.show()

#Defining the Perceptron model
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class Perceptron():
  def __init__(self, num_features):
    self.num_features = num_features
    self.weights = torch.zeros(num_features, 1,dtype=torch.float32, device=device)
    self.bias = torch.zeros(1, dtype=torch.float32, device=device)

    # placeholder vectors so they don't
    # need to be recreated each time
    self.ones = torch.ones(1)
    self.zeros = torch.zeros(1)

  def forward(self, x):
      # Implement the forward pass of the Perceptron
      z = torch.mm(x, self.weights) + self.bias
      predictions = torch.where(z > 0, torch.ones(1, dtype=torch.float32, device=device), torch.zeros(1, dtype=torch.float32, device=device))
      return predictions


  def backward(self, x, y):
    predictions = self.forward(x)
    errors = y - predictions
    return errors

  def train(self, x, y, epochs):
    for e in range(epochs):
      for i in range(y.shape[0]):
        # use view because backward expects a matrix (i.e., 2D tensor)
        errors = self.backward(x[i].reshape(1, self.num_features), y[i]).reshape(-1)
        self.weights += (errors * x[i]).reshape(self.num_features, 1)
        self.bias += errors

  def evaluate(self, x, y):
    predictions = self.forward(x).reshape( 1)
    accuracy = torch.sum(predictions == y ).float() / y.shape[0]
    return accuracy

#Training the Perceptron
ppn = Perceptron(num_features=2)
X_train_tensor = torch.tensor(X_train, dtype=torch.float32, device=device)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32, device=device)

ppn.train(X_train_tensor, y_train_tensor, epochs=5)
print('Modelparameters:')
print(' Weights: %s' % ppn.weights)
print(' Bias: %s' % ppn.bias)

#Evaluating the model
X_test_tensor = torch.tensor(X_test, dtype=torch.float32, device=device)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32, device=device)

test_acc = ppn.evaluate(X_test_tensor, y_test_tensor)
print('Test set accuracy: %.2f%%' % (test_acc*100))

w, b = ppn.weights, ppn.bias

# 2D Decision Boundary
x0_min = -2
x1_min = ((-(w[0] * x0_min) - b[0]) / w[1])
x0_max = 2

x1_max = ((-(w[0] * x0_max) - b[0]) / w[1])

fig, ax = plt.subplots(1, 2, sharex=True, figsize=(7, 3))

ax[0].plot([x0_min, x0_max], [x1_min, x1_max])
ax[1].plot([x0_min, x0_max], [x1_min, x1_max])

ax[0].scatter(X_train[y_train==0, 0], X_train[y_train==0, 1], label='class 0', marker='o')
ax[0].scatter(X_train[y_train==1, 0], X_train[y_train==1, 1], label='class 1', marker='s')

ax[1].scatter(X_test[y_test==0, 0], X_test[y_test==0, 1], label='class 0', marker='o')
ax[1].scatter(X_test[y_test==1, 0], X_test[y_test==1, 1], label='class 1', marker='s')
ax[1].legend(loc='upper left')
plt.show()
