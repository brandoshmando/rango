from django.contrib import admin
from rangoapp.models import Category, Page, UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin ):
  prepopulated_fields = {'slug': ('name',)}