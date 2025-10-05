from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)} # Auto populate the slug field based on the title field.
    list_filter = ("author","rating",)
    list_display = ("title","author","rating","is_bestselling")

admin.site.register(Book, BookAdmin)  # Register the Book model with custom admin
admin.site.register(Author)  # Register the Author model
