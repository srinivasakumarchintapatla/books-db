from django.shortcuts import  get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
        books = Book.objects.all().order_by('-rating')
        num_books = books.count()
        avg_rating = books.aggregate(Avg("rating"))#rating__avg, rating__max, rating__min
        return render(request, "book_outlet/index.html", {
        "books": books,
        "totlal_number_of_books": num_books,
        "avarage_rating": avg_rating
    })

def book_detail(request, pk): # Changed from slug to pk
#  def book_detail(request, pk): # Changed from slug to pk
    # This will query by ID (pk) and automatically raise a 404 if not found.
    # book = get_object_or_404(Book, slug=slug)
    book = get_object_or_404(Book, pk=pk)
_
    return render(request, "book_outlet/book_detail.html", {
        "book": book,
        "title": book.title, 
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling 
    })
