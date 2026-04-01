from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Language(models.Model):  # A novidade do elenco!
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Framework(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    languages = models.ManyToManyField(Language, blank=True)   # Relação N-N
    frameworks = models.ManyToManyField(Framework, blank=True) # Relação N-N
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', null=True, blank=True)
    
    github_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    live_demo = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category.name}"