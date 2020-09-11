import django_tables2 as tables
from .models import Table1, Newsfeed
from django.shortcuts import redirect, render
from django.db.models import Q, Sum
import datetime
def table_list(request):
    if request.method == 'GET':
        all_data = Table1.objects.all()
        newsfeed = Newsfeed.objects.all().first()
        columns = {
            'Name': 'name',
            'Phone Number': 'phone',
            'Birthday': 'bday',
            'E-mail': 'mail',
            'Blackboard': 'blackboard',
            'Created Date': 'created_on',
            'Updated Date': 'updated_on',
        }

        context = {
            'datas': all_data,
            'columns': columns,
            'newsfeed': newsfeed
        }
	
    return render(request, 'tableapp/people.html', context=context)

def filter_list(request):
	search_value = request.POST.get('search_value')
	filters = Table1.objects.filter(
		Q(name=search_value) |
		Q(phone=search_value)
		).distinct()
	columns = {
            'Name': 'name',
            'Phone Number': 'phone',
            'Birthday': 'bday',
            'E-mail': 'mail',
            'Blackboard': 'blackboard',
            'Created Date': 'created_on',
            'Updated Date': 'updated_on',
        }
	context = {
		'filters': filters,
		'columns': columns
	}
	return render(request, 'tableapp/people.html', context=context)