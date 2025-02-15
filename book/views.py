from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    DeleteView, 
    UpdateView
    )
from .models import Book  # Book => データベース名　(@models.py)
from django.contrib.auth import logout

# Create your views here.
class ListBookView(ListView): # ListViewを継承：データ一覧機能
    template_name = 'book/book_list.html'
    model = Book
    
class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category') # fields attribute for CreateView
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')


def index_view(request):
    object_list = Book.objects.order_by('category')
    return render(request, 'book/index.html', {'object_list':object_list})

def logout_view(request):
    logout(request)
    return redirect('index')