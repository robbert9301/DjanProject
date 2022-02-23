from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required

from accountapp.forms import AccountUpdateForm, RegistrationForm
from accountapp.models import CustomUser
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]


def hello_world(request):
    if request.method == "POST":

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        return render(request, 'accountapp/hello_world.html')


class AccountCreateView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    success_url = reverse_lazy(
        'articleapp:list')  # account creation에 성공했다면 그이후에 어디로 연결할 것인지에 대한 구문 & class에서는 reverse를 쓰지 못한다
    template_name = 'accountapp/create.html'

    def form_valid(self, form):
        temp_account = form.save(commit=False)
        temp_account.user = self.request.user
        temp_account.save()
        return super().form_valid(form)


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = CustomUser
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = CustomUser
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:list')

# @login_required
# def update(request):
#     if request.method == 'POST':
#         form = AccountUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('accountapp:detail', request.user.pk)
#     else:
#         form = AccountUpdateForm(instance=request.user)
#     context = {
#         'form': form
#     }
#     return render(request, 'accountapp/update.html', context)


@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        # 키워드인자명을 함께 써줘도 가능
        # password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('accountapp:detail', request.user.pk)

    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accountapp/password.html', {
        'password_change_form': password_change_form
    })


# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# class AccountUpdateView(UpdateView):
#     model = CustomUser
#     context_object_name = 'target_user'
#     form_class = AccountChangeForm
#     success_url = reverse_lazy('articleapp:list') #account creation에 성공했다면 그이후에 어디로 연결할 것인지에 대한 구문 & class에서는 reverse를 쓰지 못한다
#     template_name = 'accountapp/change.html'
