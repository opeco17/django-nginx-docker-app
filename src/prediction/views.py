from django.shortcuts import render
from django.views import generic

from prediction.forms import NameForm


class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        name_form = NameForm()
        context = {
            'key': 'Hello Prediction',
            'name_form': name_form,
            'login_status': request.user.is_authenticated,
        }
        return render(request, 'prediction/index.html', context)


class ResultView(generic.View):
    def post(self, request, *args, **kwargs):
        return render(request, 'prediction/result.html')