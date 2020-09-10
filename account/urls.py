from django.urls import re_path, include
from . import views

urlpatterns = [
    # previous login view
    # re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'', include('django.contrib.auth.urls')),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),
    re_path(r'^$', views.dashboard, name='dashboard'),
]
