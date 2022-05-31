from django.db import models


class Userinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20,default=1)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_pwd = models.CharField(max_length=20, blank=True, null=True)

class Businessinfo(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True )  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=45,blank=True, null=True)  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estimated_load_date = models.DateField(db_column='Estimated_Load_Date', blank=True,
                                           null=True)  # Field name made lowercase.
    pre_etd = models.DateField(db_column='Pre_ETD', blank=True, null=True)  # Field name made lowercase.
    etd = models.DateField(db_column='ETD', blank=True, null=True)  # Field name made lowercase.
    eta = models.DateField(db_column='ETA', blank=True, null=True)  # Field name made lowercase.
    vessel_voyage = models.CharField(db_column='Vessel_Voyage', max_length=45)  # Field name made lowercase.
    pol = models.CharField(db_column='POL', max_length=20)  # Field name made lowercase.
    pod = models.CharField(db_column='POD', max_length=20)  # Field name made lowercase.
    businessinfocol = models.CharField(db_column='BusinessInfocol', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numctrs = models.IntegerField(db_column='NumCtrs')  # Field name made lowercase.
    type_ctrs = models.CharField(db_column='Type_Ctrs', max_length=10)  # Field name made lowercase.
    booking_no = models.CharField(db_column='Booking_No', max_length=45)  # Field name made lowercase.
    master_no = models.CharField(db_column='Master_No', max_length=45, blank=True,null=True)  # Field name made lowercase.
    first_hbl_no = models.CharField(db_column='First_Hbl_No', max_length=45,blank=True,null=True)  # Field name made lowercase.
    hbl_memo = models.CharField(db_column='Hbl_Memo', max_length=45, blank=True,null=True)  # Field name made lowercase.
    num_hbls = models.IntegerField(db_column='Num_HBLs', blank=True, null=True)  # Field name made lowercase.
    container_no = models.CharField(db_column='Container_No', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    shipping_line = models.CharField(db_column='Shipping_Line', max_length=20)  # Field name made lowercase.
    freeddday = models.IntegerField(db_column='FreeDDday')  # Field name made lowercase.
    cost_org = models.FloatField(db_column='Cost_Org', blank=True, null=True)  # Field name made lowercase.
    sale_org = models.FloatField(db_column='Sale_Org', blank=True, null=True)  # Field name made lowercase.
    set_org = models.FloatField(db_column='Set_Org', blank=True, null=True)  # Field name made lowercase.
    local_org = models.FloatField(db_column='Local_Org', blank=True, null=True)  # Field name made lowercase.
    venta_dest = models.FloatField(db_column='Venta_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_description = models.CharField(db_column='CostHBL_Dest_Description', max_length=45, blank=True,
                                                null=True)  # Field name made lowercase.
    costhbl_dest = models.FloatField(db_column='CostHBL_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_status = models.CharField(db_column='CostHBL_Dest_Status', max_length=10)  # Field name made lowercase.
    topaid_org_description = models.CharField(db_column='Topaid_Org_Description', max_length=45, blank=True,
                                              null=True)  # Field name made lowercase.
    topaid_org = models.FloatField(db_column='Topaid_Org', blank=True, null=True)  # Field name made lowercase.
    topaid_status = models.CharField(db_column='Topaid_Status', max_length=10)  # Field name made lowercase.
    toinvoice_dest_description = models.CharField(db_column='ToInvoice_Dest_Description', max_length=45, blank=True,
                                                  null=True)  # Field name made lowercase.
    toinvoice_dest = models.FloatField(db_column='ToInvoice_Dest', blank=True, null=True)  # Field name made lowercase.
    toinvoice_dest_status = models.CharField(db_column='ToInvoice_Dest_Status',
                                             max_length=10)  # Field name made lowercase.
    profit = models.FloatField(blank=True, null=True)
    hbl_canjeado_status = models.CharField(db_column='HBL_Canjeado_Status', max_length=10)  # Field name made lowercase.
    devolution_ctrs_inidate = models.DateField(db_column='Devolution_Ctrs_IniDate', blank=True,
                                               null=True)  # Field name made lowercase.
    devolution_ctrs_findate = models.DateField(db_column='Devolution_Ctrs_FinDate', blank=True,
                                               null=True)  # Field name made lowercase.
    operation_status = models.CharField(db_column='Operation_Status', max_length=10)  # Field name made lowercase.
    bl_type = models.CharField(db_column='BL_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='Release_Type', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    mblfile = models.FileField(db_column='MBLFile', upload_to='MBLs-%Y%m/', blank=True, null=True) # Field name made lowercase.
    hblfiles = models.FileField(db_column='HBLFiles', upload_to='HBLs-%Y%m/', blank=True,null=True)  # Field name made lowercase.

    dp_voucher = models.FileField(db_column='DP_Voucher', upload_to='DPVs-%Y%m/', blank=True,null=True)  # Field name made lowercase.
    dp_invoice = models.FileField(db_column='DP_Invoice', upload_to='DPIs-%Y%m/', blank=True,null=True)  # Field name made lowercase.
    hp_voucher = models.FileField(db_column='HP_Voucher', upload_to='HPVs-%Y%m/', blank=True,null=True)  # Field name made lowercase.
    hp_invoice = models.FileField(db_column='HP_Invoice', upload_to='HPIs-%Y%m/', blank=True, null=True)  # Field name made lowercase.
    hbls_canjeados = models.FileField(db_column='HBLs_Canjeados', upload_to='HBLCNJDs-%Y%m/', blank=True, null=True)  # Field name made lowercase.

    income_voucher = models.FileField(db_column='Income_Voucher', upload_to='INVs-%Y%m/', blank=True, null=True)  # Field name made lowercase.
    income_invoice = models.FileField(db_column='Income_Invoice', upload_to='INI-%Y%m/', blank=True, null=True)  # Field name made lowercase.

    hbls_firmados = models.FileField(db_column='HBLs_Firmados', upload_to='HBLCFRMDs-%Y%m/', blank=True,null=True)  # Field name made lowercase.

class ClienteInfo(models.Model):
    id = models.CharField(db_column='id', max_length=45, primary_key=True)
    clientname = models.CharField(db_column='ClientName', max_length=45)
    clientrut = models.CharField(db_column='ClientRut', max_length=20)
    clientgiro = models.CharField(db_column='ClientGiro', max_length=200)
    clientaddress = models.CharField(db_column='ClientAddress', max_length=200)
    clientcity = models.CharField(db_column='ClientCity', max_length=45)
    clientstate = models.CharField(db_column='ClientState', max_length=45)
    clientcontact = models.CharField(db_column='ClientContact', max_length=45)

class Exportationinfo(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estimated_load_date = models.DateField(db_column='Estimated_Load_Date', blank=True,
                                           null=True)  # Field name made lowercase.
    pre_etd = models.DateField(db_column='Pre_ETD', blank=True, null=True)  # Field name made lowercase.
    etd = models.DateField(db_column='ETD', blank=True, null=True)  # Field name made lowercase.
    eta = models.DateField(db_column='ETA', blank=True, null=True)  # Field name made lowercase.
    vessel_voyage = models.CharField(db_column='Vessel_Voyage', max_length=45)  # Field name made lowercase.
    pol = models.CharField(db_column='POL', max_length=20)  # Field name made lowercase.
    pod = models.CharField(db_column='POD', max_length=20)  # Field name made lowercase.
    businessinfocol = models.CharField(db_column='BusinessInfocol', max_length=200, blank=True,
                                       null=True)  # Field name made lowercase.
    numctrs = models.IntegerField(db_column='NumCtrs')  # Field name made lowercase.
    type_ctrs = models.CharField(db_column='Type_Ctrs', max_length=10)  # Field name made lowercase.
    booking_no = models.CharField(db_column='Booking_No', max_length=45)  # Field name made lowercase.
    master_no = models.CharField(db_column='Master_No', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    first_hbl_no = models.CharField(db_column='First_Hbl_No', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    hbl_memo = models.CharField(db_column='Hbl_Memo', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    num_hbls = models.IntegerField(db_column='Num_HBLs', blank=True, null=True)  # Field name made lowercase.
    container_no = models.CharField(db_column='Container_No', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    shipping_line = models.CharField(db_column='Shipping_Line', max_length=20)  # Field name made lowercase.
    freeddday = models.IntegerField(db_column='FreeDDday')  # Field name made lowercase.
    cost_org = models.FloatField(db_column='Cost_Org', blank=True, null=True)  # Field name made lowercase.
    sale_org = models.FloatField(db_column='Sale_Org', blank=True, null=True)  # Field name made lowercase.
    set_org = models.FloatField(db_column='Set_Org', blank=True, null=True)  # Field name made lowercase.
    local_org = models.FloatField(db_column='Local_Org', blank=True, null=True)  # Field name made lowercase.
    venta_dest = models.FloatField(db_column='Venta_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_description = models.CharField(db_column='CostHBL_Dest_Description', max_length=45, blank=True,
                                                null=True)  # Field name made lowercase.
    costhbl_dest = models.FloatField(db_column='CostHBL_Dest', blank=True, null=True)  # Field name made lowercase.
    costhbl_dest_status = models.CharField(db_column='CostHBL_Dest_Status', max_length=10)  # Field name made lowercase.
    topaid_org_description = models.CharField(db_column='Topaid_Org_Description', max_length=45, blank=True,
                                              null=True)  # Field name made lowercase.
    topaid_org = models.FloatField(db_column='Topaid_Org', blank=True, null=True)  # Field name made lowercase.
    topaid_status = models.CharField(db_column='Topaid_Status', max_length=10)  # Field name made lowercase.
    toinvoice_dest_description = models.CharField(db_column='ToInvoice_Dest_Description', max_length=45, blank=True,
                                                  null=True)  # Field name made lowercase.
    toinvoice_dest = models.FloatField(db_column='ToInvoice_Dest', blank=True, null=True)  # Field name made lowercase.
    toinvoice_dest_status = models.CharField(db_column='ToInvoice_Dest_Status',
                                             max_length=10)  # Field name made lowercase.
    profit = models.FloatField(blank=True, null=True)
    hbl_canjeado_status = models.CharField(db_column='HBL_Canjeado_Status', max_length=10)  # Field name made lowercase.
    devolution_ctrs_inidate = models.DateField(db_column='Devolution_Ctrs_IniDate', blank=True,
                                               null=True)  # Field name made lowercase.
    devolution_ctrs_findate = models.DateField(db_column='Devolution_Ctrs_FinDate', blank=True,
                                               null=True)  # Field name made lowercase.
    operation_status = models.CharField(db_column='Operation_Status', max_length=10)  # Field name made lowercase.
    bl_type = models.CharField(db_column='BL_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='Release_Type', max_length=45, blank=True,
                                    null=True)  # Field name made lowercase.
    mblfile = models.FileField(db_column='MBLFile', upload_to='MBLs-%Y%m/', blank=True,
                               null=True)  # Field name made lowercase.
    hblfiles = models.FileField(db_column='HBLFiles', upload_to='HBLs-%Y%m/', blank=True,
                                null=True)  # Field name made lowercase.

    dp_voucher = models.FileField(db_column='DP_Voucher', upload_to='DPVs-%Y%m/', blank=True,
                                  null=True)  # Field name made lowercase.
    dp_invoice = models.FileField(db_column='DP_Invoice', upload_to='DPIs-%Y%m/', blank=True,
                                  null=True)  # Field name made lowercase.
    hp_voucher = models.FileField(db_column='HP_Voucher', upload_to='HPVs-%Y%m/', blank=True,
                                  null=True)  # Field name made lowercase.
    hp_invoice = models.FileField(db_column='HP_Invoice', upload_to='HPIs-%Y%m/', blank=True,
                                  null=True)  # Field name made lowercase.
    hbls_canjeados = models.FileField(db_column='HBLs_Canjeados', upload_to='HBLCNJDs-%Y%m/', blank=True,
                                      null=True)  # Field name made lowercase.

    income_voucher = models.FileField(db_column='Income_Voucher', upload_to='INVs-%Y%m/', blank=True,
                                      null=True)  # Field name made lowercase.
    income_invoice = models.FileField(db_column='Income_Invoice', upload_to='INI-%Y%m/', blank=True,
                                      null=True)  # Field name made lowercase.

    hbls_firmados = models.FileField(db_column='HBLs_Firmados', upload_to='HBLCFRMDs-%Y%m/', blank=True,
                                     null=True)  # Field name made lowercase.

