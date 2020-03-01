from django.shortcuts import render, redirect
from django.views import generic

from prediction import models
from prediction.machine_learning.logic import Logic
from prediction.machine_learning.rnn import RNN
from prediction.forms import NameForm
import torch

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        name_form = NameForm()
        context = {
            'key': 'Hello Prediction',
            'name_form': name_form,
        }
        return render(request, 'prediction/index.html', context)


class ResultView(generic.View):
    def post(self, request, *args, **kwargs):
        display_num = 5
        language_probability_list = []
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            rnn = RNN(input_size=57, hidden_size=128, output_size=18)
            rnn.load_state_dict(torch.load('./prediction/machine_learning/rnn'))
            logic = Logic(rnn)
            probability_list, language_list = logic(name, display_num)
            language_probability_list = [[language_list[i], round(probability_list[i] * 100, 1)] for i in range(display_num)]
            models.NameTable.objects.create(name=name, nation=language_list[0])
            context = {
                'name': name,
                'language_probability_list': language_probability_list,
            }
            return render(request, 'prediction/result.html', context)
        else:
            return redirect('index')