# from django_tables2 import SingleTableView
import django_tables2 as tables
from .models import Table, Newsfeed
# from .tables import TableTable
# from django_filters.views import FilterView
# from django_tables2.views import SingleTableMixin
from .filterset import PersonFilter
from django.shortcuts import redirect, render
from django.db.models import Q, Sum
import datetime
# class TableListView(SingleTableView):
#     model = Table
#     table_class = TableTable
#     template_name = 'tableapp/people.html'
# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = TableTable
#     model = Table
#     template_name = 'tableapp/people.html'

#     filterset_class = PersonFilter
def table_list(request):
    print("==========", datetime.datetime.now().strftime ("%Y%m%d"))
    if request.method == 'GET':
        all_data = Table.objects.all()
        newsfeed = Newsfeed.objects.all().first()
        print(">>>>>>>>>>>>>>", newsfeed)

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
	filters = Table.objects.filter(
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