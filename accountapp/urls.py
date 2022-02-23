from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from accountapp.views import AccountCreateView, AccountDetailView, AccountDeleteView, AccountUpdateView

app_name = "accountapp"

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'), #class는 accountcrateview를 써야한다
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), #primary key를 받아야한다
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('password/', views.password, name='password')
]