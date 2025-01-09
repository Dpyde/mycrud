# from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Book,Author
from .serializer import BookSerializer,UserSerializer,AuthorSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class book_list(APIView):
    def get(self,request,format=None):
        books = Book.objects.all()
        serializer_class =BookSerializer(books,many=True)
        return Response(serializer_class.data)
    def post(self,request,format=None):
        serializer_class=BookSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

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
 
class login(APIView):
    def post(self,request):
        user=get_object_or_404(User,username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'detial':'Not found.'},status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)
        serializer=UserSerializer(instance=user)
        return Response({ "token":token.key,"user":serializer.data })

class signup(APIView):
    def post(self,request,format=None):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token= Token.objects.create(user=user)
            return Response({"token":token.key,"user":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class author_list(APIView):
    def get(self,request,format=None):
        authors = Author.objects.all()
        serializer_class =AuthorSerializer(authors,many=True)
        return Response(serializer_class.data)
    def post(self,request,format=None):
        serializer_class=AuthorSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)