from django.contrib import admin
# Register your models here.
#from .forms import CounterCreateForm
from .views import CounterCreateForm
# Register your models here.
from .models import Counter




class CounterCreateAdmin(admin.ModelAdmin):
    list_display = ['quantities', 'date', 'values_to_receive', 'total', 'total_to_receive', 'author']
    form = CounterCreateForm
    list_filter = ['date']





'''
class PerfilCreateAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    form = PerfilCreateForm
    list_filter = ['date']

'''   

admin.site.register(Counter, CounterCreateAdmin)