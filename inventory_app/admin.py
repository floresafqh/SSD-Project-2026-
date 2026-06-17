from django.contrib import admin
from .models import InventoryItem, AuditLog

# Configure a clean view layout for inventory tracking
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

# Configure a restricted read-only administrative view for your logs
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'details')
    search_fields = ('user', 'action')
    list_filter = ('action', 'timestamp')
    
    # Security Best Practice: Prevent administrators from tempering with or modifying the system audit trails
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False