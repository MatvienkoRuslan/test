from django.urls import path

from . import views
from .views import signup, login_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout, name='logout')
]
