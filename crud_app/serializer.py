from rest_framework import serializers
from .models import Book,Author
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','email']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields='__all__'