
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('people/', views.by_age, name="age"),
    path('people/<int:x>', views.by_id, name="people"),
    ]