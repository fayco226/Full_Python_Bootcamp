
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home, name="home"),
    path('visit/',views.visitor, name="visitor"),
    path('addVisitor', views.addVisitor, name="addVisitor")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


