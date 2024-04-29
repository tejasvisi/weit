# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet, TaskViewSet, TaskCompletionViewSet
from .custom_admin import custom_admin_site
from . import views

router = DefaultRouter()
router.register(r'android-apps', AndroidAppViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'task-completions', TaskCompletionViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Auth views
    path('api-auth/', include('rest_framework.urls')),
    
    # User facing views
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('custom-admin/', views.adminprofile,name='adminprofile'),
]
