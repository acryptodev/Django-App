import django_tables2 as tables
from .models import Table1, Newsfeed
from django.shortcuts import redirect, render
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.core import serializers
import datetime
import json

from django.apps import apps 



def table_list(request):
    if request.method == 'GET':
        all_data = Table1.objects.all()
        newsfeed = Newsfeed.objects.all().first()
        app_tables = list(apps.all_models['tableapp'])
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
            'newsfeed': newsfeed,
            'tablenames': app_tables,
            'selectedtable': 'table1'
        }
    
    return render(request, 'tableapp/people.html', context=context)

def filter_list(request):
    search_value = request.POST.get('search_value')
    app_tables = list(apps.all_models['tableapp'])
    model_name = ''
    if "model" in request.session:
        model_name = request.session["model"]
    filters = None
    if model_name:
        for c in apps.get_app_configs():
                for m in c.get_models():
                    if m._meta.model_name == model_name:
                        filters = m._meta.concrete_model.objects.filter(
                                        Q(name__icontains=search_value)
                                        ).distinct()
        columns = request.session["columns"]
        context = {
            'filters': filters,
            'columns': columns,
            'tablenames': app_tables,
            'selectedtable': model_name
        }
        return render(request, 'tableapp/people.html', context=context)
    else:
        filters = Table1.objects.filter(
            Q(name__icontains=search_value) |
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
            'columns': columns,
            'tablenames': app_tables,
            'selectedtable': model_name
        }
        return render(request, 'tableapp/people.html', context=context)

def get_table_data(request):
    if request.method == 'POST':
        for c in apps.get_app_configs():
            for m in c.get_models():
                if m._meta.model_name == request.POST["name"]:
                    request.session["model"] = m._meta.model_name
                    get_records = m._meta.concrete_model.objects.values()
                    columns = []
                    columns_dict = {}
                    for each_field in m._meta.fields:
                        if each_field.name == 'id':
                            columns.append('No')
                        else:
                            columns.append(each_field.name.replace('_', ' ').capitalize())
                        if each_field.name == 'id':
                            columns_dict['No'] = 'no'
                        else:
                            columns_dict[each_field.name.replace('_', ' ').capitalize()] = each_field.name
                    request.session["columns"]= columns_dict
                    data = list(get_records)
                    return JsonResponse({"data": data, "columns": columns}, safe=False)