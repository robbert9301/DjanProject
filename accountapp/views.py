from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accountapp.forms import RegistrationForm
from accountapp.models import CustomUser


def hello_world(request):

    if request.method == "POST":

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        return render(request, 'accountapp/hello_world.html')


class AccountCreateView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    success_url = reverse_lazy('accountapp:hello_world')  # account creation에 성공했다면 그이후에 어디로 연결할 것인지에 대한 구문 & class에서는 reverse를 쓰지 못한다
    template_name = 'accountapp/create.html'
