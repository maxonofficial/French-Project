from django.urls import path,include
from . import views1
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/',views1.register_view,name="register"),
    path('login/',views1.LoginAPIView.as_view(),name="login"),
    path('logout/', views1.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
