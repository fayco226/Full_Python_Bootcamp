from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('animals/', views.home, name='home'),
    path('family/<int:x>', views.family, name="family" ),
    path('animal/<int:y>', views.animals, name="animal")
]
