from django.urls import path, include
from .views import home, aboutus, ourmenu, ourservices, allergydevices
urlpatterns = [
    path('', home, name='home'),
    path('aboutus', aboutus, name='aboutus'),
    path('ourmenu', ourmenu, name='ourmenu'),
    path('ourservices', ourservices, name='ourservices'),
    path('allergydevices', allergydevices, name='allergydevices'),
    
]
