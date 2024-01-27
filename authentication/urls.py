from django.urls import path
from . import views

urlpatterns = [
      path("auth/login/google/", GoogleLoginApi.as_view(), 
         name="login-with-google"),
]
