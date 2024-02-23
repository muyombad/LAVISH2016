from django.urls import  path
from lavish import views




urlpatterns = [
    path('', views.home, name='home'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('log_out', views.log_out, name = 'log_out1'),
    path('mtn', views.mtn, name = 'mtn'),
    path('airtell', views.airtell, name = 'airtell'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('tatal', views.tatal, name='tatal'),
    path('stationry', views.stationary, name='stationary'),
    path('mtn_statment', views.mtn_statment, name='mtn_statment'),
    path('airtell_statment', views.airtell_statment, name='airtell_statment'),
    path('change_password_eproy', views.change_password_emproy, name='change_password_eproy'),
]