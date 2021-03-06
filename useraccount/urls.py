from django.urls import path, include

from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views #to use with Class-based Views

from . import views

app_name = 'useraccount'


urlpatterns = [


  

    path('register/', views.register, name='register'),
    #login logout urpls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('useraccount:password_change_done')),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),



    # reset password urls
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', success_url=reverse_lazy("useraccount:password_reset_done")),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html",success_url = reverse_lazy('useraccount:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


    path('edit/', views.edit, name='edit'),

    path('', views.dashboard, name='dashboard'),

    path('budget/', views.my_budget, name='budget'),

    path('cost/', views.my_cost, name='cost'),


]
