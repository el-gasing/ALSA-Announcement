from django.urls import path

from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('loading/', views.loading_page, name='loading'),
    path('department/', views.department_page, name='department'),
    path('department-internal/', views.department_internal_page, name='department_internal'),
    path('department-external/', views.department_external_page, name='department_external'),
]
