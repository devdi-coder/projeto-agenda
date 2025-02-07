from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone','email',
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', 'email',
    list_per_page = 10
    list_max_show_all = 50
    list_editable = 'first_name', 'last_name', 'phone',