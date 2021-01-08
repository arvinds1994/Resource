from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('addresource/', views.add_resource, name='addresource'),
    path('resourcelist/', views.view_resource, name='resourcelist'),
    path('update/<id>', views.update_view, name='update'),
    path('delete/<id>', views.delete_view, name='delete'),
]