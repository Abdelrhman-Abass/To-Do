from django.urls import include, path
from rest_framework import routers
from django.conf.urls import include
from rest_framework_simplejwt import views

from .views import *

# app_name = 'tasks'

# router = routers.DefaultRouter()
# router.register(r'tasks',TaskSerializer, basename='tasks')
# router.register(r'users',UserSerializer, basename='users')

urlpatterns = [
    path(r'api/token/', views.TokenObtainPairView.as_view()),
    # path('loginapi/', LoginView.as_view(), name='customelogin'),
    path(r'api/token/refresh/', views.TokenRefreshView.as_view()),
    path(r'users/tasks/<str:username>/', UserTasks.as_view()),
    path(r'tasks/operation/<int:pk>/', TaskOperations.as_view()),
    path(r'tasks/list/',ALLTaskList.as_view(), name='tasks'),

    path('tasks/', Tasks.as_view(), name='tasks'),
    path('done/', Done_Tasks.as_view(), name='done-tasks'),
    path('add/', AddBookView.as_view(), name='add'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
]