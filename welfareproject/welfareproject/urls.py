"""welfareproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view(),name='main'),
    path('user_reg/',views.user_reg.as_view(),name='user_reg'),
    path('add_though/',views.add_though.as_view(),name='add_though'),
    path('view_though/',views.view_though,name='view_though'),
    path('add_event/',views.add_event.as_view(),name='add_event'),
    path('view_event/',views.view_event,name='view_event'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('approval_users/',views.approval_users,name='approval_users'),
    path('delete_data/',views.delete_data,name='delete_data'),
    path('update_data/',views.update_data,name='update_data'),
    path('accepted_users/',views.accepted_users,name='accepted_users'),
    path('rejected_users/',views.rejected_users,name='rejected_users'),
    path('adm_logout/',views.adm_logout,name='adm_logout'),
    path('admin_login/',views.admin_login,name='admin_login')

]
