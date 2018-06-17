from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from posts.models import Post


@register(Post)
class PostAdmin(admin.ModelAdmin):

    admin.site.site_header = 'WordPlease Admin'
    admin.site.site_title = 'WordPlease Admin'
    admin.site.index_title = 'Dashboard'
