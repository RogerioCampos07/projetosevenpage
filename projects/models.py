from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Stack(models.Model): # Unificado e poderoso!
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    # Relação ManyToMany: Um projeto tem várias stacks, uma stack está em vários projetos
    stacks = models.ManyToManyField(Stack, blank=True, related_name='projects')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    
    github_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    live_demo = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category.name}"