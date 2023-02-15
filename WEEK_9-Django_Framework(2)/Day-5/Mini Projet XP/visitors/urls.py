
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home, name="home"),
    
    path('visit/',views.visitor, name="visitor"),
    path('addVisitor', views.visitor, name="addVisitor"),
    path("editVisitor/<id>/", views.visitor, name="editVisitor"),
    path("deleteVistor/<id>/", views.visitor, name="deleteVisitor"),
    
    path('bedroom/', views.bedroom, name='bedroom'),
    path('bedroom/detail/<id>',views.bedroom, name='bedroomid' ),
    path('addBedroom/', views.bedroom, name='addBedroom' ),
    path("editBedroom/<id>", views.bedroom, name="editBedroom"),
    path("deleteBedroom/<id>/", views.bedroom, name="deleteBedroom"),
    
    path('book/', views.book, name="book"),
    path('addBook/', views.book, name="addBook"),
    path("editBook/<id>", views.book, name="editBook"),
    path("deleteBook/<id>/", views.book, name="deleteBook"),
    
    path('bedroom_size/', views.bedroom_size, name="bedroom_size"),
    path('addBedroom_size/', views.bedroom_size, name="addBedroom_size"),
    path("editBedroom_size/<id>/", views.bedroom_size, name="editBedroom_size"),
    path("deleteBedroom_size/<id>/", views.bedroom_size, name="deleteBedroom_size"),
    
    path("review/", views.review, name="review"),
    path("addReview/", views.review, name="addReview"),
    path("editReview/<id>", views.review, name="editReview"),
    path("deleteReview/<id>/", views.review , name="deleteReview"),
    
    
    path("bedroom_type/", views.bedroom_type , name="bedroom_type"),
    path("addBedroom_type/", views.bedroom_type , name="addBedroom_type"),
    path("editBedroom_type/<id>", views.bedroom_type , name="editBedroom_type"),
    path("deleteBedroom_type/<id>", views.bedroom_type , name="deleteBedroom_type"),
    
    path("simple_review/", views.simple_review, name="simple_review"),
    path("addSimple_review/", views.simple_review, name="addSimple_review"),
    path("editSimple_review/<id>", views.simple_review, name="editSimple_review"),
    path("deleteSimple_review/<id>/", views.simple_review , name="deleteSimple_review"),
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


