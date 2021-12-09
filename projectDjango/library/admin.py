from django.contrib import admin
from .models import Lh
from .models import St
from .models import Book

# Register your models here.

class LhAdmin(admin.ModelAdmin):
    list_display = ('short_Name', 'full_Name') 
    list_display_links = ('short_Name', 'full_Name') 
    search_fields = ('short_Name', 'full_Name') 

class StAdmin(admin.ModelAdmin):
    list_display = ('index', 'short_Name') 
    list_display_links = ('index', 'short_Name') 
    search_fields = ('index','short_Name') 

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'listAuthor', 'tom', 'part', 'isbn', 'year', 'index', 'shelfSt', 'count') 
    list_display_links = ('name',)
    search_fields = ('name', 'listAuthor', 'isbn', 'index')

admin.site.register(Lh, LhAdmin)
admin.site.register(St, StAdmin) 
admin.site.register(Book, BookAdmin)
