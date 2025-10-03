from django.urls import path
from . import views

app_name = 'book_outlet'

urlpatterns = [
    path("", views.index, name="index"),
    # path("<slug:slug>/", views.book_detail, name="book_detail")
     path("<int:pk>/", views.book_detail, name="book_detail")
]
