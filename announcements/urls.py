from django.urls import path

from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('loading/', views.loading_page, name='loading'),
    path('department/', views.department_page, name='department'),
]
