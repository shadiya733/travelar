from django.urls import path,include
from . import views
from . views import register
app_name='credentails'
urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
