from django.contrib import admin
from .models import Table
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin

class TableAdmin(ImportExportModelAdmin):
	list_display = ['name', 'phone', 'mail', 'blackboard', 'created_on', 'updated_on']
	list_per_page = 10
	list_editable = ['blackboard',]
	search_fields = ['name', 'phone', 'mail',]
	fields = [('name', 'phone', 'mail'), ('bday'), ('blackboard')]
	def has_delete_permission(self, request, obj = None): 
		return False


admin.site.register(Table, TableAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
