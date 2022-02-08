from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Reaction)
admin.site.register(Commit)
