from django.contrib import admin

from .models import Menu, MenuItem
# Register your models here.

class MenuItemAdmin(admin.StackedInline):
	model = MenuItem
	min_num = 1
	extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	inlines = [
		MenuItemAdmin
	]