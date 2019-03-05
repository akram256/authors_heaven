from django.urls import path
from rest_framework.schemas import get_schema_view

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
    VerifyAccount, ResetPasswordView, ChangePasswordView
)
schema_view = get_schema_view(title='Authors haven')
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/verify/', VerifyAccount.as_view()),
    path('schema/', schema_view),
    path('password-reset/', ResetPasswordView.as_view()),
    path('password-reset/<token>/', ResetPasswordView.as_view()),
    path('password/reset/done/', ChangePasswordView.as_view()),

]
