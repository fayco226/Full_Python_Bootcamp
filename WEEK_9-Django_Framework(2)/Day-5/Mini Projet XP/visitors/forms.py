from .models import Visitor, Bedroom_size, Bedroom_type, Bedroom, Book, Review, Simple_Reviews
from django.forms import ModelForm
class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class Bedroom_typeForm(ModelForm):
    class Meta:
        model = Bedroom_type
        fields = '__all__'
        
class Bedroom_sizeForm(ModelForm):
    class Meta:
        model = Bedroom_size
        fields = '__all__'

class BedroomForm(ModelForm):
    class Meta:
        model = Bedroom
        fields = ['type_bedroom', 'size_bedroom',
                  'cost', 'photo',]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
    
class Simple_reviewForm(ModelForm):
    class Meta:
        model = Simple_Reviews
        fields = '__all__'



    


