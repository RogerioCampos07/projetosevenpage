from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Language, Framework, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 1. Adicionamos a visualização da imagem na lista
    list_display = ('get_thumbnail', 'title', 'category', 'framework', 'created_at')
    list_filter = ('category', 'languages', 'frameworks', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('languages', 'frameworks')
    
    # 2. Navegação rápida por data
    date_hierarchy = 'created_at'
    
    # 3. Organização Visual dos Campos (Fieldsets)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'category', 'description', 'thumbnail')
        }),
        ('Tecnologias', {
            'fields': ('languages', 'frameworks'),
            'description': 'Selecione as linguagens e frameworks utilizados.'
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