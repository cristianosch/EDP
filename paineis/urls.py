from django.urls import path
from . import views
#from . views import PostListView
from django.urls import include

app_name = 'paineis'

urlpatterns = [
    path('', views.home, name='home'),
    path('quantity/', views.quantity, name='quantity'),    
    path('add_panel/', views.add_panel, name='add_panel'),  
    #path('total_a_receber/', views.total_a_receber, name='total_a_receber'),  
    #path('accounts/', include('registration.backends.default.urls')),   
]