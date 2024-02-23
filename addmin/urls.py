from addmin import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('otp', views.otp, name='otp'),
    path('admin_dashboard', views.admin_home, name='admin_home'),
    path('logout_admin', views.logout_admin, name='logout_admin'),
    path('user_profile_super', views.user_profile_super, name='user_profile_super'),
    path('rerequest', views.rerequest_otp, name='rerequest_otp'),
    path('rest', views.rest, name = 'rest'),
    path('credit_or_debit', views.credit_or_debit, name = 'credit_or_debit'),
    path('change_password', views.change_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
