from django.contrib import admin
from .models import Post


admin.site.site_header = 'Posts Admin'
admin.site.index_title = 'Posts Admin Area'
admin.site.site_title = 'Welcome to the posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_filter = ('title', 'publiced_date', )
	list_display = ('title', 'publiced_date')
	ordering = ('-publiced_date', )