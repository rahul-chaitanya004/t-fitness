from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about'),
    path('membership/', views.membership, name='membership'),
    path('confirmation/<int:membership_id>/', views.confirmation, name='confirmation'),
     path('trainer/', views.trainer, name='trainer'),
]
