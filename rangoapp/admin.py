from django.contrib import admin
from rangoapp.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin ):
  prepopulated_fields = {'slug': ('name',)}