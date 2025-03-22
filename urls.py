from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('portfolio/', login_required(views.portfolio_view), name='portfolio'),
      # Login required for portfolio
    path('about/', views.about, name='about'),
]
