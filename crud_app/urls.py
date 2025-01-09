from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list.as_view(), name='book_list'),
    path('book/<int:pk>/', views.book_detail.as_view(), name='book_detail'),
    path('login', views.login.as_view(), name='login'),
    path('reg', views.signup.as_view(), name='reg'),
    path('author', views.author_list.as_view(), name='author'),
    # path('new/', views.book_create, name='book_create'),
    # path('<int:pk>/edit/', views.book_update, name='book_update'),
    # path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]