import numpy as np
import torch
from torch.utils.data import Dataset


def _data_filter(df, type, year=None):
    if year is not None:
        df = df.loc[df['year'] == year]
    return df.loc[df['type'] == type]

class GasDataset(Dataset):
    def __init__(self, df, seq_len):
        self.df = df
        self.seq_len = seq_len
    
    def __len__(self):
        return len(self.df) - self.seq_len - 1

    def __getitem__(self, idx):
        data = self.df.iloc[idx:idx + self.seq_len]
        x = torch.from_numpy(np.array(data[['supply']], dtype=np.float32))
        y = torch.from_numpy(np.array(self.df.iloc[idx + self.seq_len, -1], dtype=np.float32))

        return x, y

def make_dataset(df, seq_len, train_rate, type, year=None):
    df = _data_filter(df, type, year)
    train_len = int(len(df) * train_rate)
    train_df, val_df = df[:train_len], df[train_len:]
    train_dataset = GasDataset(train_df, seq_len)
    if train_rate < 1.0:
        val_dataset = GasDataset(val_df, seq_len)
    else:
        val_dataset = None
    print(f'train_rate: {train_rate} train_len: {len(train_dataset)}, val_len: {len(val_dataset)}')

    return train_dataset, val_dataset