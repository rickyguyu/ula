from django.contrib import admin
from .models import Businessinfo
from .models import ClienteInfo

from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Businessinfo)
class BusinessinfoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'clientname', 'pre_etd','eta','vessel_voyage',
                     'pol','pod','type_ctrs', 'booking_no','master_no',
                    'container_no','shipping_line','operation_status','toinvoice_dest_description','toinvoice_dest_status','costhbl_dest_description','costhbl_dest_status',
                    'topaid_org_description','topaid_status','hbl_canjeado_status','freeddday')
    ordering = ('id', 'clientname', 'pre_etd','eta','vessel_voyage',
                     'pol','pod','type_ctrs', 'booking_no','master_no',
                    'container_no','shipping_line','operation_status','costhbl_dest_status',
                    'topaid_status','toinvoice_dest_status','hbl_canjeado_status')
    search_fields = ('id','clientname','pre_etd','eta','vessel_voyage', 'booking_no','master_no','container_no','shipping_line')
    pass

# Register your models here.
@admin.register(ClienteInfo)
class ClienteInfoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('clientname', 'clientrut', 'clientgiro','clientcontact')
    ordering = ('clientname','clientrut')
    search_fields = ('clientname','clientrut','clientcontact')
    pass

# admin.site.register(Businessinfo)
