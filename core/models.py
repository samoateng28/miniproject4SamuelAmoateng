from django.db import models
from django.contrib.auth import get_user_model

# Get the active user model
User = get_user_model() 

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def comment_count(self):
        """Returns the number of approved comments for this post"""
        return self.comments.filter(approved=True).count()


class Comment(models.Model):
    """
    Model for storing comments on blog posts.
    Each comment is linked to a specific post and user.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)  # Set to False if you want comment moderation
    
    class Meta:
        ordering = ['created_on']  # Oldest comments first
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'