from django.db import models
import datetime

class Category(models.Model):
    title = models.CharField(max_length = 30 , help_text='max of 30 characters')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/category_image' , blank=True , null = True)
    about= models.CharField(max_length = 100 , help_text = "max of 100 characters" , blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Author(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    display_image = models.ImageField(upload_to='media/dp' , blank=True , null = True)
    cover_image = models.ImageField(upload_to='media/cover' , blank=True , null = True)
    about = models.TextField()
    

    def __str__(self):
        return self.first_name +" "+ self.last_name 
class Post(models.Model):
    title = models.CharField(max_length = 30 , help_text='max of 30 characters')
    story = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/post' , blank=True , null = True)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , null = True)
    author = models.ForeignKey(Author , on_delete = models.CASCADE , null = True)

    def __str__(self):
        return  self.title
    
    