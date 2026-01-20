from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in admin list view
    list_display = ('username', 'email', 'is_staff', 'is_active', 'account_status')
    
    # Fields to filter by
    list_filter = ('is_staff', 'is_active', 'account_status', 'is_superuser')

    # Field sets for the detail/edit view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('currency', 'timezone', 'language')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Account Status', {'fields': ('account_status', 'is_email_verified', 'two_factor_enabled', 'last_login_ip')}),
    )

    # Fields to show when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(UserProfile)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user','profile_completed',)