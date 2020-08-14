import django_tables2 as tables
from .models import Table

class TableTable(tables.Table):
    class Meta:
        model = Table
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'phone', 'bday', 'mail', 'blackboard', 'created_on', 'updated_on' )
        attrs = {"class": "table table-responsive"}