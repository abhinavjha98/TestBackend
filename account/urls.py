from django.contrib import admin
from django.urls import path
from account import views
from account.views import UserAuthView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('signup/',UserAuthView.as_view({'post':'signup'})),
    path('login/', UserAuthView.as_view({'post': 'login'})),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verfiytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
