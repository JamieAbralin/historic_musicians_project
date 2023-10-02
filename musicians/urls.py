# musicians/urls.py
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('musicians/', views.musician_list, name='musician_list'),
    path('musicians/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
]
