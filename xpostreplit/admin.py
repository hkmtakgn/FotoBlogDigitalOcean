from django.contrib import admin
from xpostreplit.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "file",
    ]
