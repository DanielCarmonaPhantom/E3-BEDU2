"""USERS app url configuration"""

from django.urls import path

from . import views

app_name='users'
urlpatterns = [
    path("", views.login_view, name='login')
]
