from django.contrib import admin
from .models import Articles,Category,Tag

class ArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author","img","abstract","visited","created_at")
    search_fields=("title","author","abstract","content",)
    list_filter=list_display
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)