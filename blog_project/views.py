from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import UserRegisterForm, PostForm
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.http import Http404


@login_required
def add_post(request, id=None):
    if id:
        post = Post.objects.get(id=id)
        if post.author != request.user:
            return redirect('user_articles')
    else:
        post = None
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('user_articles')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/add_post.html', {'form': form, 'post': post})



@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':  
        if post.author == request.user:
            post.delete()
        return redirect('home')  
    
    return render(request, 'blog/delete_post.html', {'post': post}) 

def search(request):
    query = request.GET.get('query', '')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts})

@login_required(login_url='login')
def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('login')

    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/user_articles.html', {'posts': posts})

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:5]  
    return render(request, 'home.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  
    
    return render(request, 'logout.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    
    def get_object(self, queryset=None):
        """Override to ensure only post owners can edit."""
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if post.author != self.request.user:
            raise Http404("Nie masz uprawnień do edytowania tego posta")
        return post

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_articles')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

@login_required   
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)


    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

