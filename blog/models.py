
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from tinymce.models import HTMLField
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
    
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField() # Change This Line
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag)    
    category = models.ForeignKey(
            Category,
            on_delete=models.SET_DEFAULT,
            default=1
        )
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        # If the author is not set, set it to the current user
        if not self.author_id:
            self.author = User.objects.get(username='current_user_username')
        super().save(*args, **kwargs)


