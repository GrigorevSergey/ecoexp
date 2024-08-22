from django.contrib import admin

from application.models import Post, PostValue

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['customer', 'contract', 'name_of_the_object']
    list_filter = ['contract']
    search_fields = ['contract', 'name_of_the_object']



@admin.register(PostValue)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'value', 'name_of_indicators']


