# Note this file was not created by default (python manage.py startapp); I manually added it

from django.urls import path
from . import views
import re

# change the urls to make sense later
#
urlpatterns = [
    path('', views.toLogin_view),
    path('login/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    # path('imports/', views.importsmain),
    path('exports/', views.exportsmain),
    # path('imports/newBusinessImport/', views.newbusinessimport),
    path('exports/newBusinessExport/', views.newbusinessexport),
    # path('imports/saveBusinessImport/', views.savebusinessimport),
    path('exports/saveBusinessExport/', views.savebusinessexport),
    # path('imports/search/', views.searchimports),
    path('exports/search/', views.searchexports),
    path('exports/export/', views.exportbusiness, name='export'),
    # path('imports/import/', views.importbusiness, name='import'),
    # path('imports/delbusiness/', views.delbusinessimport),
    path('exports/delbusiness/', views.delbusinessexport),

    # From Ricky
    path('prealerta/', views.prealerta),
    path('profile/', views.profile)
]