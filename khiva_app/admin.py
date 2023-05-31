from django.contrib import admin
from .models import Khiva, Category, Contact, Images, Restaurant, KhivaNews


@admin.register(Khiva)
class khivaAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Contact)
admin.site.register(Images)
admin.site.register(Restaurant)
admin.site.register(KhivaNews)