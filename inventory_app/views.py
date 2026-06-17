from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import InventoryItem, AuditLog

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        if not username or not password:
            messages.error(request, "All fields are mandatory.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'register.html')

        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        User.objects.create_user(username=username, password=password)
        AuditLog.objects.create(action="USER_REGISTRATION", user=username, details="Account registered successfully.")
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            AuditLog.objects.create(action="LOGIN_SUCCESS", user=username, details="Successful authentication session established.")
            return redirect('dashboard')
        else:
            # Audit log logging failed login attempt without recording plaintext credentials
            AuditLog.objects.create(action="LOGIN_FAILED", user=username, details="Unauthorized authentication attempt intercepted.")
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        quantity = request.POST.get('quantity', '0')
        price = request.POST.get('price', '0.00')
        try:
            new_item = InventoryItem(name=name, quantity=quantity, price=price)
            new_item.full_clean()
            new_item.save()
            AuditLog.objects.create(action="ITEM_CREATED", user=request.user.username, details=f"Item added: {name}")
            messages.success(request, f"Successfully added '{name}' to secure stock inventory!")
            return redirect('dashboard')
        except Exception:
            AuditLog.objects.create(action="VALIDATION_BYPASS_ATTEMPT", user=request.user.username, details=f"Rejected out-of-bounds dataset injection attempt.")
            messages.error(request, "Input Validation Error: Please check your formatting rules.")
            return redirect('dashboard')

    items = InventoryItem.objects.all()
    return render(request, 'dashboard.html', {'items': items})

@login_required(login_url='login')
def edit_item_view(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        old_name = item.name
        item.name = request.POST.get('name', '').strip()
        item.quantity = request.POST.get('quantity', '0')
        item.price = request.POST.get('price', '0.00')
        try:
            item.full_clean()
            item.save()
            AuditLog.objects.create(action="ITEM_UPDATED", user=request.user.username, details=f"Updated item ID {item_id}: {old_name} -> {item.name}")
            messages.success(request, f"Successfully updated '{item.name}'!")
            return redirect('dashboard')
        except Exception:
            AuditLog.objects.create(action="VALIDATION_BYPASS_ATTEMPT", user=request.user.username, details=f"Rejected malicious entry alteration attempt.")
            messages.error(request, "Validation Error: Please check your input formatting rules.")
            return redirect('edit_item', item_id=item.id)
    return render(request, 'edit_item.html', {'item': item})

@login_required(login_url='login')
def delete_item_view(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    item_name = item.name
    item.delete()
    AuditLog.objects.create(action="ITEM_DELETED", user=request.user.username, details=f"Deleted item: {item_name}")
    messages.success(request, f"Successfully deleted '{item_name}' from inventory.")
    return redirect('dashboard')

# Profile View Module
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')

# Restricted Audit Log View Module
@login_required(login_url='login')
def audit_logs_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit_logs.html', {'logs': logs})

def logout_view(request):
    if request.user.is_authenticated:
        AuditLog.objects.create(action="USER_LOGOUT", user=request.user.username, details="User closed active secure session context.")
    logout(request)
    return redirect('login')