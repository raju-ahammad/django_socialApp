from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import User, UserProfile

class NewUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['first_name' ,'last_name', 'username', 'email',]
    model = User

admin.site.register(User, NewUserAdmin)


class UserAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


#class UserProfileAdmin(BaseUserAdmin):
    #model = UserProfile
    #list_display = ('user', 'blood_group', 'gender', 'phone', 'city',)
    #ordering = ('blood_group',)
    #search_fields = ('blood_group', 'user', 'gender', 'city',)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'gender', 'phone', 'city',)
    search_fields = ('blood_group', 'user', 'gender', 'city',)
    list_filter   = ('blood_group',)
    ordering = ('blood_group',)

admin.site.register(UserProfile, UserProfileAdmin)
