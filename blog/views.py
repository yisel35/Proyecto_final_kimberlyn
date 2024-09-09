from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm, UserProfileForm

# Página principal
def home(request):
    return render(request, 'blog/home.html')

# Lista de publicaciones
@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detalle de una publicación con comentarios
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

# Crear una nueva publicación
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# Ver el perfil de usuario
@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Si no existe el perfil, redirige a la página de edición
        return redirect('edit_profile')

    return render(request, 'blog/profile.html', {'user_profile': user_profile})

# Editar o crear perfil de usuario
@login_required
def edit_profile(request):
    # Obtiene o crea un perfil de usuario
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil del usuario

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'blog/edit_profile.html', {'form': form})

def sobre_mi(request):
    return render(request, 'blog/sobre_mi.html')