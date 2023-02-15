from django.contrib import admin
from .models import Visitor, Bedroom, Bedroom_size, Bedroom_type, Book, Review, Simple_Reviews
# Register your models here.
admin.site.register(Visitor)
admin.site.register(Bedroom)
admin.site.register(Bedroom_size)
admin.site.register(Bedroom_type)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Simple_Reviews)