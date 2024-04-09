"""
URL configuration for gym_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.ilogin, name='ilogin'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('join_plan/', views.join_plan, name='join_plan'),
    path('handle_join_plan/', views.handle_join_plan, name='handle_join_plan'),
    path('my_plan/', views.my_plan, name='my_plan'),
    path('edit_plan/', views.edit_plan, name='edit_plan'),
    path('handle_edit_plan/', views.handle_edit_plan, name='handle_edit_plan'),
    path('delete_plan/', views.delete_plan, name='delete_plan'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)