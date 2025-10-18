from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Reader)
admin.site.register(Borrow)
admin.site.register(Publisher)
admin.site.register(LibraryBranch)