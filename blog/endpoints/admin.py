from django.contrib import admin

from .models import Post, Contributor, Features, Skill, Admin

admin.site.register(Post)
admin.site.register(Contributor)
admin.site.register(Features)
admin.site.register(Skill)
admin.site.register(Admin)