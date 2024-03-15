"""
URL configuration for image_caption_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app4 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
   

    path('adminhome/', views.adminhome,name="adminhome"),
    path('manage_user/', views.manage_user,name="manage_user"),
    path('accept/<int:id>', views.accept,name="accept"),
    path('adminreview/',views.adminreview,name="adminreview"),
    path('addawareness/',views.addawareness,name="addawareness"),
    path('admin_viewawareness/',views.admin_viewawareness,name="admin_viewawareness"),
    path('edit_awareness/',views.edit_awareness,name="edit_awareness"),



    path('parenthome/',views.parenthome,name="parenthome"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('editprofile/<int:id>',views.editprofile,name="editprofile"),
    path('changepw/',views.changepw,name="changepw"),
    path('vision/',views.vision,name="vision"),
    path('addreview/',views.addreview,name="addreview"),
    path('parentreview/',views.parentreview,name="parentreview"),
    path('parent_viewawareness/',views.parent_viewawareness,name="parent_viewawareness"),
    path('addchild/',views.addchild,name="addchild"),
    path('editchild/<int:id>',views.editchild,name="editchild"),
    path('parent_viewchild/',views.parent_viewchild,name="parent_viewchild"),
    


    path('childhome/',views.childhome,name="childhome"),
    path('vision2/',views.vision2,name="vision2"),

]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)