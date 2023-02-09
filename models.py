import torch.nn as nn

class TensorExtractor(nn.Module):
    def forward(self, x):
        tensor, _ = x
        return tensor

class Model(nn.Module):
    def __init__(self, model_name, input_size, hidden_size, num_layer, conv_size=None):
        super(Model, self).__init__()
        model_layers = []
        if conv_size is not None:
            conv = nn.Conv1d(input_size, conv_size, kernel_size=4, stride=2, padding=0)
            model_layers.append(conv)
            input_size = input_size
        if model_name == 'lstm':
            model_layers.append(nn.LSTM(input_size, hidden_size, num_layer))
        elif model_name == 'gru':
            model_layers.append(nn.GRU(input_size, hidden_size, num_layer))
        elif model_name == 'rnn':
            model_layers.append(nn.RNN(input_size, hidden_size, num_layer))

        model_layers.append(TensorExtractor())
        model_layers.append(nn.Linear(hidden_size, 1))
        self.model = nn.Sequential(*model_layers)
    
    def forward(self, x):
        return self.model(x)