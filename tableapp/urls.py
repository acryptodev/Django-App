from django.urls import path
from .views import table_list, filter_list, get_table_data
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tableapp'

urlpatterns = [
    path('', table_list),
    path('tableapp/search', filter_list, name='tableapp-search'),
    path('get_table_data', get_table_data, name='get_table_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)