from django.urls import path
from . import views

app_name = 'book_outlet'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.book_detail, name='book_detail')
]
