from .views import EmailValidationView, RegistrationView, UsernameValidationView, LoginView, LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LoginView.as_view(),name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name="validate_email"),
]