from django.contrib import admin
from .models import Article, Network
# Register your models here.





class NetworkInline(admin.StackedInline):
    model = Network
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [
        NetworkInline,
    ]
    def _networks(self, obj):
        return obj.projects.all()

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    save_on_top = True