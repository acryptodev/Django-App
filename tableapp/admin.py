from django.contrib import admin
from .models import Table1, Table2, Table3, Newsfeed
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin

class Table1Admin(ImportExportModelAdmin):
	list_display = ['name', 'phone', 'mail', 'created_on', 'updated_on']
	list_per_page = 10
	search_fields = ['name', 'phone', 'mail',]
	fields = [('name', 'phone', 'mail'), ('bday')]
	# def has_delete_permission(self, request, obj = None): 
	# 	return False
class Table2Admin(ImportExportModelAdmin):
	list_display = ['name', 'gender', 'interests', 'created_on', 'updated_on']
	list_per_page = 10
	search_fields = ['name',]
	fields = [('name', 'gender'), ('interests')]
class Table3Admin(ImportExportModelAdmin):
	list_display = ['name', 'university', 'created_on', 'updated_on']
	list_per_page = 10
	search_fields = ['name', 'university',]
	fields = [('name', 'university'),]

admin.site.register(Table1, Table1Admin)
admin.site.register(Table2, Table2Admin)
admin.site.register(Table3, Table3Admin)
admin.site.register(Newsfeed)
admin.site.unregister(User)
admin.site.unregister(Group)
