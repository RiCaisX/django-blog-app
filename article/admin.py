from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["id","title","author","created_date","content_type"]
    
    list_display_links = ["title","created_date"]
    
    search_fields = ["title"]

    list_filter = ["created_date","author","content_type"]
    class Meta:
        model = Article

