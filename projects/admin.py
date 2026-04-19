from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Project, Stack

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 1. Adicionamos a visualização da imagem na lista
    list_display = ('get_thumbnail', 'title', 'category', 'created_at')
    list_filter = ('category', 'stacks', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('stacks',) 
    
    date_hierarchy = 'created_at'
    
    # 3. Organização Visual dos Campos (Fieldsets)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'category', 'stacks', 'description', 'thumbnail')
        }),
        
        ('Links e Demonstração', {
            'classes': ('collapse',), # Essa seção começa escondida (mais limpo!)
            'fields': ('github_link', 'youtube_link', 'live_demo'),
        }),
    )

    # Função para exibir a imagem na listagem do Admin
    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.thumbnail.url)
        return "Sem imagem"
    get_thumbnail.short_description = 'Capa'