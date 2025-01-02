from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.response import Response
from django.http import Http404
from .models import Book
from .forms import BookForm
from .serializer import BookSerializer


# List View
class book_list(APIView):
    def get(self,request,format=None):
        books = Book.objects.all()
        serializer_class =BookSerializer(books,many=True)
        return Response(serializer_class.data)
        # return render(request, 'book_list.html', {'books': books})
    def post(self,request,format=None):
        serializer_class=BookSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

# Detail View
class book_detail (APIView):
    def get_object(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # book = get_object_or_404(Book, pk=pk)
    # return render(request, 'book_detail.html', {'book': book})


# Create View
# def book_create(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'book_form.html', {'form': form})

# # Update View
# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'book_form.html', {'form': form})

# # Delete View
# def book_delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'book_confirm_delete.html', {'book': book})