"""PoliceTrainSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps.index import views as index_views
from rbac.views import UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('user.urls')),  # user下的路由交给user.urls处理
    path('index', index_views.index_view),
    re_path('^rbac/', include('rbac.urls', namespace='rbac')),
]
