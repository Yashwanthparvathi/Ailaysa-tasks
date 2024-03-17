from django.contrib import admin
from ailaysaapp.models import UserProfile, Category,PostModel, CommentModel
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
# admin.site.register(Subcategory)
admin.site.register(PostModel)
admin.site.register(CommentModel)