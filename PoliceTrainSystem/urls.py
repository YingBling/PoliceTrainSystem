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
from django.urls import path, include
from django.views.generic import TemplateView

from index import views as index_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user.urls')),  # user下的路由交给user.urls处理
    path('api/subject/', include('subjectManagement.urls')),
    path('index', index_views.index_view),
    path('api/', include('app.urls')),
    path('', TemplateView.as_view(template_name='index.html')),  # 路由到index.html
    # path('api-auth/', include('rest_framework.urls')),
]
