from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostUpdateView, register
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search_results'),
    path('moje-artykuly/', views.user_articles, name='user_articles'),
    path('dodaj-artykul/', views.add_post, name='add_post'),
    path('usun-artykul/<int:id>/', views.delete_post, name='delete_post'),
    path('edytuj-artykul/<int:post_id>/', views.edit_post, name='edit_post'),

]
