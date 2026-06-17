from django.contrib import admin
from django.urls import path
from inventory_app.views import (
    register_view, login_view, dashboard_view, logout_view, 
    edit_item_view, delete_item_view, profile_view, audit_logs_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('item/edit/<int:item_id>/', edit_item_view, name='edit_item'),
    path('item/delete/<int:item_id>/', delete_item_view, name='delete_item'),
    path('profile/', profile_view, name='profile'),
    path('audit-logs/', audit_logs_view, name='audit_logs'),
]