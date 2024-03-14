
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
from torch.autograd import Variable
import matplotlib.pyplot as plt

df = pd.read_csv('RTX_new.csv')

prices = df['Adj Close'].values.reshape(-1, 1)

data_size = len(prices)

train_ratio = 0.8
train_size = int(data_size * train_ratio)

seq_length = 5


train_data = prices[:train_size]
test_data = prices[train_size - seq_length:]

scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data)
test_data_normalized = scaler.transform(test_data)

def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L-tw):
        train_seq = input_data[i:i+tw]
        train_label = input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq ,train_label))
    return inout_seq

train_inout_seq = create_inout_sequences(train_data_normalized, seq_length)

class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]


# %%
model = LSTM()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 150
all_losses = []

for i in range(epochs):
    total_loss = 0
    for seq, labels in train_inout_seq:
        seq = torch.FloatTensor(seq).view(-1, 1, 1)
        labels = torch.FloatTensor(labels)

        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

        total_loss += single_loss.item()
    
    avg_loss = total_loss / len(train_inout_seq)
    all_losses.append(avg_loss)


    if i%25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')


plt.figure(figsize=(10,5))
plt.plot(all_losses, label='Training loss')
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()


test_predictions = []
model.eval()

seq_length = 5
test_inout_seq = create_inout_sequences(test_data_normalized, seq_length)

with torch.no_grad():
    for seq, _ in test_inout_seq:
        seq = torch.FloatTensor(seq).view(-1, 1, 1)
        y_pred = model(seq)
        test_predictions.append(y_pred.item())


predicted_prices = scaler.inverse_transform(np.array(test_predictions).reshape(-1, 1))

plt.figure(figsize=(12,6))
plt.plot(test_data, label='True Prices')
plt.plot(predicted_prices, label='Predicted Prices', linestyle='--')
plt.title('Comparison of True Prices and Predictions')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()





