from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dahsboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.view_reord, name='record'),
    path('delete-record/<int:pk>', views.delete_reord, name='delete-record')

]