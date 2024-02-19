from django.urls import path 
#from myapp import views

from .views import ImmobileList,ImmobileCreate,ClientCreate,LocationCreate,ReportsList

urlpatterns = [
    path('', ImmobileList.as_view(), name='list-location'), 
    path('form-immobile/', ImmobileCreate.as_view(), name='immobile-create'),
    path('form-client/', ClientCreate.as_view(), name='client-create'),    
    path('form-location/<int:id>/', LocationCreate.as_view(), name='location-create'), 
    path('reports/', ReportsList.as_view(), name='reports'),
]


