from django.contrib import admin
from .models import *

class SubcategoryTabular(admin.TabularInline):
    model = subCategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryTabular]

class AdditionalinfoTabular(admin.TabularInline):
    model = Additional_information

class AdditionalImageTabular(admin.TabularInline):
    model = Additional_image

class ProductAdmin(admin.ModelAdmin):
    inlines = [AdditionalinfoTabular,AdditionalImageTabular]

# Register your models here.
admin.site.register(Slider)
admin.site.register(mainCategory)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)