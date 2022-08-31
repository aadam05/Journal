"""default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app.views import *

# Для JWT токенов
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Для автоматической маршрутизации вьюсетов
from rest_framework import routers

# автоматическая маршрутизация
# router = routers.DefaultRouter()
# router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Заменяет строчки снизу которые на данном этапе в малом количестве
    #path('api/v1/', include(router.urls)),

    # Standard django session auth
    #path('api/v1/drf-auth', include('rest_framework.urls')),

    # Djoser token auth
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

    # JWT token auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # обычные urls
    path('api/v1/articleList/', ArticleAPIList.as_view()),
    path('api/v1/articleList/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('api/v1/articleDestroy/<int:pk>/', ArticleAPIDestroy.as_view()),
]
