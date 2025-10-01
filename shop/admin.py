from django.contrib import admin
from .models import Product,Order
# Register your models here.


admin.site.site_header = "E-Commerce Admin"   # Customizing the admin site header
admin.site.site_title = "E-Commerce Admin Portal"   # Customizing the admin site title
admin.site.index_title = "Welcome to E-Commerce Admin Portal"   # Customizing the admin index title


class ProductAdmin(admin.ModelAdmin):   # Customizing the admin interface for Product model
    
    
    list_display = ('title','price','discount_price','category','description')

    search_fields = ('title','category')   # Adding search functionality for title and category fields
    
    
    def action_category_to_default(self, request, queryset):
        queryset.update(category='Default')   # Custom action to set category to 'Default'
    
    
    actions=('action_category_to_default')  # Registering the custom action
    
    
    action_category_to_default.short_description = "Default Category"   # Description for the custom action
    # fields=('title','price')   # Fields to display in the admin form
    
    list_editable = ('price','discount_price')   # Making price and discount_price fields editable in the list view
    
    
admin.site.register(Product,ProductAdmin)   #  Registering the Product model with the customized admin interface
admin.site.register(Order)