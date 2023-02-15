from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Visitor, Bedroom_type, Bedroom_size, Bedroom, Book, Review, Simple_Reviews
from .forms import VisitorForm, Bedroom_sizeForm, Bedroom_typeForm, BookForm, BedroomForm, ReviewForm, Simple_reviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required
def home(request):
    vistcount = Visitor.objects.count()
    bookcount = Book.objects.count()
    reviewcount = Review.objects.count()
    bedroom = Bedroom.objects.count()
    review = Review.objects.all()
    
    return render(request, 'admin_hotel/homeAdmin.html', {'countVisitor':vistcount, 'countBedroom':bedroom, 'countBook':bookcount, 'countReview':reviewcount, 'models':review})
@login_required
def visitor(request, id=0):
    
    if 'editVisitor' in request.path and id != 0 :
        
        model = get_object_or_404(Visitor, pk=id)
        if request.method == 'POST':
            form = VisitorForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('visitor')
            else:
                form = VisitorForm(instance=model)
                return render(request, 'admin_hotel/visitors.html', {"form": form})
        form = VisitorForm(instance=model)
        return render(request, 'admin_hotel/visitors.html', {"form": form, 'id':id})
    
    elif 'deleteVistor' in request.path and id != 0:
        ob = get_object_or_404(Visitor, id=id)
        ob.delete()
        return redirect('visitor')
            
    else:
        
    
        if request.method == "POST" and 'addVisitor' in request.path:
            form = VisitorForm(request.POST)
            visit = Visitor.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "visitor added !")
                return redirect('visitor')
            else:
                return render(request, 'admin_hotel/visitors.html', {"form": form, "models":visitor})
        else:
            form = VisitorForm()
            visit = Visitor.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            return render(request, 'admin_hotel/visitors.html', {"form": form, "models":visitor})
        
    

        
@login_required
def bedroom(request, id=0):
    if 'editBedroom' in request.path and id != 0 :
        
        model = get_object_or_404(Bedroom, pk=id)
        if request.method == 'POST':
            form = BedroomForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('bedroom')
            else:
                form = BedroomForm(instance=model)
                return render(request, 'admin_hotel/bedroom.html', {"form": form})
        form = BedroomForm(instance=model)
        return render(request, 'admin_hotel/bedroom.html', {"form": form, 'id':id})
    
    elif 'deleteBedroom' in request.path and id != 0:
        ob = get_object_or_404(Bedroom, id=id)
        ob.delete()
        return redirect('bedroom')
    
    elif 'detail' in request.path and id !=0:
        model= Bedroom.objects.filter(id=id)
        form = BedroomForm()
        return render(request, 'admin_hotel/bedroom.html', {"form": form, "models":model, "id":id})
            
    else:
        
    
        if request.method == "POST" and 'addBedroom' in request.path:
            form = BedroomForm(request.POST)
            visit = Bedroom.objects.all()
            page = Paginator(visit, 3)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "bedroom size added !")
                return redirect('bedroom')
            else:
                return render(request, 'admin_hotel/bedroom.html', {"form": form, "models":visitor})
        else:
            form = BedroomForm()
            visit = Bedroom.objects.all()
            page = Paginator(visit, 3)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            return render(request, 'admin_hotel/bedroom.html', {"form": form, "models":visitor})
    
@login_required
def bedroom_size(request, id=0):
    
    if 'editBedroom_size' in request.path and id != 0 :
        
        model = get_object_or_404(Bedroom_size, pk=id)
        if request.method == 'POST':
            form = Bedroom_sizeForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('bedroom_size')
            else:
                form = Bedroom_sizeForm(instance=model)
                return render(request, 'admin_hotel/bedroom_size.html', {"form": form})
        form = Bedroom_sizeForm(instance=model)
        return render(request, 'admin_hotel/bedroom_size.html', {"form": form, 'id':id})
    
    elif 'deleteBedroom_size' in request.path and id != 0:
        ob = get_object_or_404(Bedroom_size, id=id)
        ob.delete()
        return redirect('bedroom_size')
            
    else:
        
    
        if request.method == "POST" and 'addBedroom' in request.path:
            form = Bedroom_sizeForm(request.POST)
            visit = Bedroom_size.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "bedroom size added !")
                return redirect('bedroom_size')
            else:
                return render(request, 'admin_hotel/bedroom_size.html', {"form": form, "models":visitor})
        else:
            form = Bedroom_sizeForm()
            visit = Bedroom_size.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            return render(request, 'admin_hotel/bedroom_size.html', {"form": form, "models":visitor})
    
def bedroom_type(request, id=0):
    if 'editBedroom_type' in request.path and id != 0 :
        
        model = get_object_or_404(Bedroom_type, pk=id)
        if request.method == 'POST':
            form = Bedroom_typeForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('bedroom_type')
            else:
                form = Bedroom_typeForm(instance=model)
                return render(request, 'admin_hotel/bedroom_type.html', {"form": form})
        form = Bedroom_typeForm(instance=model)
        return render(request, 'admin_hotel/bedroom_type.html', {"form": form, 'id':id})
    
    elif 'deleteBedroom_type' in request.path and id != 0:
        ob = get_object_or_404(Bedroom_type, id=id)
        ob.delete()
        return redirect('bedroom_type')
            
    else:
        
    
        if request.method == "POST" and 'addBedroom' in request.path:
            form = Bedroom_typeForm(request.POST)
            visit = Bedroom_type.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "bedroom type added !")
                return redirect('bedroom_type')
            else:
                return render(request, 'admin_hotel/bedroom_type.html', {"form": form, "models":visitor})
        else:
            form = Bedroom_typeForm()
            visit = Bedroom_type.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            visitor = page.get_page(pge)
            return render(request, 'admin_hotel/bedroom_type.html', {"form": form, "models":visitor})
        
        
@login_required
def book(request, id=0):
    if 'editBook' in request.path and id != 0 :
        
        model = get_object_or_404(Book, pk=id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('book')
            else:
                form = BookForm(instance=model)
                return render(request, 'admin_hotel/book.html', {"form": form})
        form = BookForm(instance=model)
        return render(request, 'admin_hotel/book.html', {"form": form, 'id':id})
    
    elif 'deleteBook' in request.path and id != 0:
        ob = get_object_or_404(Book, id=id)
        ob.delete()
        return redirect('book')
            
    else:
        
    
        if request.method == "POST" and 'addBook' in request.path:
            form = BookForm(request.POST)
            visit = Book.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            book = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "bedroom type added !")
                return redirect('book')
            else:
                return render(request, 'admin_hotel/book.html', {"form": form, "models":book})
        else:
            form = BookForm()
            visit = Book.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            book = page.get_page(pge)
            return render(request, 'admin_hotel/book.html', {"form": form, "models":book})

@login_required
def review(request, id=0):
    if 'editReview' in request.path and id != 0 :
        
        model = get_object_or_404(Review, pk=id)
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('review')
            else:
                form = ReviewForm(instance=model)
                return render(request, 'admin_hotel/review.html', {"form": form})
        form = ReviewForm(instance=model)
        return render(request, 'admin_hotel/review.html', {"form": form, 'id':id})
    
    elif 'deleteReview' in request.path and id != 0:
        ab = get_object_or_404(Review, id=id)
        ab.delete()
        return redirect('review')
            
    else:
        
    
        if request.method == "POST" and 'addReview' in request.path:
            form = ReviewForm(request.POST)
            visit = Review.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            review = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Review type added !")
                return redirect('review')
            else:
                return render(request, 'admin_hotel/review.html', {"form": form, "models":review})
        else:
            form = ReviewForm()
            visit = Review.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            review = page.get_page(pge)
            return render(request, 'admin_hotel/review.html', {"form": form, "models":review})
        
        
@login_required
def simple_review(request, id=0):
    if 'editSimple_review' in request.path and id != 0 :
        
        model = get_object_or_404(Simple_Reviews, pk=id)
        if request.method == 'POST':
            form = Simple_reviewForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('simple_review')
            else:
                form = Simple_reviewForm(instance=model)
                return render(request, 'admin_hotel/simple_review.html', {"form": form})
        form = Simple_reviewForm(instance=model)
        return render(request, 'admin_hotel/simple_review.html', {"form": form, 'id':id})
    
    elif 'deleteSimple_review' in request.path and id != 0:
        ab = get_object_or_404(Simple_Reviews, id=id)
        ab.delete()
        return redirect('simple_review')
            
    else:
        
    
        if request.method == "POST" and 'addSimple_review' in request.path:
            form = Simple_reviewForm(request.POST)
            visit = Simple_Reviews.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            review = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Review type added !")
                return redirect('simple_review')
            else:
                return render(request, 'admin_hotel/simple_review.html', {"form": form, "models":review})
        else:
            form = Simple_reviewForm()
            visit = Simple_Reviews.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            review = page.get_page(pge)
            return render(request, 'admin_hotel/simple_review.html', {"form": form, "models":review})
        