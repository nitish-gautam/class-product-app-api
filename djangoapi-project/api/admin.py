from django.contrib import admin
from .models import Product

#class TodoAdmin(admin.ModelAdmin):
#    readonly_fields = ('dateupdated',)

admin.site.register(Product)
