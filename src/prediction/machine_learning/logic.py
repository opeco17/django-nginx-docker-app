import torch
import torch.nn as nn
import torch.nn.functional as F
import pickle

all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,;'"
all_categories = ['Czech', 'German', 'Arabic', 'Japanese', 'Chinese', 'Vietnamese', 'Russian', 'French', 'Irish',
                  'English', 'Spanish', 'Greek', 'Italian', 'Portuguese', 'Scottish', 'Dutch', 'Korean', 'Polish']
n_letters = len(all_letters)


def letterToIndex(letter):
    return all_letters.find(letter)


def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor


def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor


class Logic():
    def __init__(self, model):
        self.model = model

    def __call__(self, name, n_predictions):
        value = []
        category = []

        line_tensor = lineToTensor(name)
        hidden = self.model.initHidden()

        for i in range(line_tensor.size()[0]):
            output, hidden = self.model(line_tensor[i], hidden)
        top_value, top_index = F.softmax(output).topk(n_predictions)

        for i in range(n_predictions):
            value.append(top_value[0][i].item())
            category.append(all_categories[top_index[0][i].item()])
        return value, category