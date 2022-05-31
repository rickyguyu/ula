# Note this file was not created by default (python manage.py startapp); I manually added it

from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('imports/', views.importsmain),
    path('exports/', views.exportsmain),
    path('imports/newBusinessImport/', views.newbusinessimport),
    path('exports/newBusinessExport/', views.newbusinessexport),
    path('imports/search/', views.searchimports),
    path('exports/search/', views.searchexports),
    path('exports/export/', views.exportbusiness, name='export'),
    path('imports/import/', views.importbusiness, name='import'),

    path('imports/savebusinessimport/', views.savebusiness),
    path('exports/savebusinessexport/', views.savebusiness),

    # From Ricky
    path('login/', views.login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('newBusiness/', views.new_business),
    path('delbusiness/', views.delbusiness),
    path('prealerta/', views.prealerta),
    path('profile/', views.profile)
]