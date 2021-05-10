from django.contrib import admin
from publication.models import Publications, PublicationsImages, Likes


class PublicationsImagesInline(admin.TabularInline):
    model = PublicationsImages
    extra = 1


class PublicationsAdmin(admin.ModelAdmin):
    inlines = [PublicationsImagesInline]
    readonly_fields = ('date',)


admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Likes)