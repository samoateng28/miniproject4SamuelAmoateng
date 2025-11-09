# INF601 - Advanced Programming in Python
# samuel Amoateng
# Mini Project 4




from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('features/', views.features_view, name='features'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/create/', views.create_post, name='create_post'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]

