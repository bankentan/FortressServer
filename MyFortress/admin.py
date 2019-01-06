from django.contrib import admin
from MyFortress import models
# Register your models here.

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):    #創建用戶頁面中生成的的表單
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.MyUser
        #fields = ('email', 'date_of_birth', 'name', 'age', 'tel_phone')
        fields = ('email', )
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):    #修改用戶頁面生成的表單，支持修改密碼
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )

    class Meta:
        model = models.MyUser
        fields = '__all__'
        #field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial.get('password')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'name', 'is_admin')   #用戶列表頁面列出的字段
    list_filter = ('is_admin',)      #用戶列表頁面過濾的字段
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('date_of_birth', 'name', 'tel_phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser', 'user_permissions', 'groups')}),
    )        #fieldsets是用戶修改頁面中顯示的字段
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'name', 'tel_phone', 'password1', 'password2')}
        ),
    )       #add_fieldsets是新增用戶頁面中顯示的字段
    search_fields = ('email',)     #搜索的字段
    ordering = ('email',)
    filter_horizontal = ('user_permissions', 'groups')   #多對多顯示的字段

class HostListAdmin(admin.ModelAdmin):
    search_fields = ('hostname',)

admin.site.register(models.MyUser, UserAdmin)
admin.site.register(models.HostList, HostListAdmin)
admin.site.register(models.Roles)
admin.site.register(models.dev_group)
admin.site.register(models.ISP)
