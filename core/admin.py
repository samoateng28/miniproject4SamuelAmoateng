

from django.contrib import admin
from .models import Post # Import the Post model you created

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Post model 
    within the Django administration site.
    """
    
    # 1. List Display Configuration
    # Fields displayed on the main change list page
    list_display = (
        'title', 
        'author', 
        'status', 
        'created_on', 
        'updated_on',
    )
    
    # 2. Filter, Search, and Ordering
    # Fields that allow filtering in the sidebar
    list_filter = (
        'status', 
        'author', 
        'created_on',
    )
    
    # Fields that can be searched using the admin search bar
    search_fields = (
        'title', 
        'content',
    )
    
    # Automatically prepopulate the 'slug' field based on the 'title'
    prepopulated_fields = {'slug': ('title',)}
    
    # 3. Custom Action
    # Add an action to quickly set posts to 'Published'
    actions = [
        'make_published',
    ]

    def make_published(self, request, queryset):
        """Action to change selected posts status to Published."""
        # Update the selected posts status to 1 (Published)
        updated = queryset.update(status=1)
        
        # Display a success message
        self.message_user(
            request, 
            f'{updated} post(s) were successfully published.'
        )
    make_published.short_description = "Mark selected posts as Published"


    # 4. Fieldsets (Layout for the Edit/Add Page)
    # Organize fields into logical groups for a cleaner UI
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content'),
        }),
        ('Publication Details', {
            'fields': ('author', 'status'),
            'classes': ('collapse', 'wide'), # Optional: collapse this section initially
        }),
    )

    # Automatically set the 'author' field to the current logged-in user 
    # when creating a new post.
    def save_model(self, request, obj, form, change):
        if not change:
            # Set author only on creation
            obj.author = request.user
        super().save_model(request, obj, form, change)