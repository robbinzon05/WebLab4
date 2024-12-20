from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('user/update/score/', update_score, name='update_score'),  # Новый маршрут для обновления счётчика
    path('users/', UserListAPIView.as_view()),
]