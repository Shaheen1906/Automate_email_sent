from django.contrib import admin
from .models import Employee, Event, EmailLog, EmailTemplate


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Display these fields in the list view

class EventAdmin(admin.ModelAdmin):
    list_display = ('employee', 'event_type', 'event_date')  # Display these fields in the list view

class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'event', 'sent_at', 'success', 'error_message')  # Display these fields in the list view

class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'template')  # Display these fields in the list view

# Register the models with their respective admin classes
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EmailLog, EmailLogAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)