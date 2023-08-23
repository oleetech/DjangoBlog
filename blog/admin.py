from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    
admin.site.register(Post,PostAdmin)

from .models import Category
admin.site.register(Category)   

from .models import Tag
admin.site.register(Tag)