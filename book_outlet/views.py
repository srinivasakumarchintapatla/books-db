from django.shortcuts import  get_object_or_404, render
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
        books = Book.objects.all()
        return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, pk): # Changed from slug to pk
#  def book_detail(request, pk): # Changed from slug to pk
    # This will query by ID (pk) and automatically raise a 404 if not found.
    # book = get_object_or_404(Book, slug=slug)
    book = get_object_or_404(Book, pk=pk)

    return render(request, "book_outlet/book_detail.html", {
        "book": book,
        "title": book.title, 
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling 
    })
