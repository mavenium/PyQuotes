from django.contrib import admin

from Web.models import Person, Category, Quote

# Register Person model
admin.site.register(Person)

# Register Category model
admin.site.register(Category)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['content', 'person', 'display_category']
    Quote.display_category.short_description = 'Categories'


# Register Quote model
admin.site.register(Quote, QuoteAdmin)
