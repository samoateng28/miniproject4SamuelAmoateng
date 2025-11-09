# INF601 - Advanced Programming in Python
# samuel Amoateng
# Mini Project 4



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.defaultfilters import slugify 

from core.forms import ContactForm
from core.models import Post

from core.forms import PostForm



def home_view(request):
    """
    Retrieves published blog posts and prepares them for the homepage template.
    """

    published_posts = Post.objects.filter(status=1).order_by('-created_on')
    

    context = {
        # The first published post for the main 'Featured' section
        'latest_post': published_posts.first(), 
        
        # The next six posts for the 'Recently Published' grid (1:7 means elements at index 1 up to, but not including, 7)
        'recent_posts': published_posts[1:7] 
    }
    

    return render(request, 'pages/home.html', context)




def post_detail(request, slug):
    """
    Displays the full content of a single blog post.
    """

    post = get_object_or_404(Post, slug=slug, status=1)

    recent_posts = Post.objects.filter(status=1).exclude(slug=slug).order_by('-created_on')[:4]
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'pages/post_detail.html', context)



@login_required(login_url='login')
def logoutpage(request):
    print("logged out")
    logout(request)
    messages.success(request, 'You are Logged out')
    return redirect('login')


def about_view(request):
    return render(request, 'pages/about.html')


def features_view(request):
    return render(request, 'pages/features.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            messages.success(request, 'Thanks for contacting us! We will respond within 48 hours.')
            return redirect('contact') 
        else:
            # If invalid, the form object is passed back to the template 
            # with errors attached.
            messages.error(request, 'Please correct the errors below and fill out all required fields.')
    
    else:
        form = ContactForm()
        
    return render(request, 'pages/contact.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'pages/dashboard.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False) 

            post.author = request.user 
            
            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            post.slug = slug

            post.save()
            
            messages.success(request, f'Post "{post.title}" successfully created!')
            

            return redirect('dashboard') 
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:

        form = PostForm()
        
    context = {
        'form': form,
        'title': 'Create New Post'
    }
    return render(request, 'pages/create_post.html', context)