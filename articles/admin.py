from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author","img","abstract","visited","created_at")
    search_fields=("title","author","abstract","content",)
    list_filter=list_display
admin.site.register(Articles,ArticlesAdmin)