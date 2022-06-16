from django.db import models
import datetime


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
    # Id and Op Status
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    operation_status = models.CharField(db_column='Operation_Status', default="NO", max_length=10)
    # Vessel Information - booking, carrier, vessel, delivery terminal
    booking_no = models.CharField(db_column='Booking_No', max_length=45)  # Field name made lowercase.
    shipping_line = models.CharField(db_column='Shipping_Line', max_length=20)  # Field name made lowercase.
    vessel_voyage = models.CharField(db_column='Vessel_Voyage', max_length=45)  # Field name made lowercase.
    delivery_terminal = models.CharField(db_column='Delivery_Terminal', max_length=200)  # Field name made lowercase.

    # Port Information (Port Names)
    pol = models.CharField(db_column='POL', max_length=20)  # Field name made lowercase.
    pol_sailing = models.CharField(db_column='POL_Sailing', max_length=20)  # Field name made lowercase.
    pod_discharge = models.CharField(db_column='POD_Discharge', max_length=20)  # Field name made lowercase.
    pod = models.CharField(db_column='POD', max_length=20)  # Field name made lowercase.

    # Date Information
    # Ricky wants to change Input Format - %d-%m-%Y %H:%M
    pickup_ctrs = models.DateTimeField(blank=True, null=True, db_column='pickup_ctrs', max_length=20)   # Field name made lowercase.
    cutoff_docmatriz = models.DateTimeField(blank=True, null=True, db_column='cutoff_docmatriz', max_length=20)
    cutoff_vgm = models.DateTimeField(blank=True, null=True, db_column='Cutoff_VGM', max_length=20)
    cargo_cutoff = models.DateTimeField(blank=True, null=True, db_column='Cargo_Cutoff', max_length=20)
    stacking_start = models.DateTimeField(blank=True, null=True, db_column='Stacking_Start', max_length=20)
    stacking_close = models.DateTimeField(blank=True, null=True, db_column='Stacking_Close', max_length=20)
    etd = models.DateField(blank=True, null=True, db_column='ETD')  # Field name made lowercase.
    eta = models.DateField(blank=True, null=True, db_column='ETA')  # Field name made lowercase.

    # Container and Package Information
    package_type = models.CharField(db_column='Package_Type/s', max_length= 50) # e.j. MAQUILLAJES
    type_ctrs = models.CharField(db_column='Type_Ctrs', max_length=10)  # e.j. 40'HQ
    qty = models.CharField(db_column='Qty.', max_length=20)
    id_number = models.CharField(db_column='Id_Number', max_length=75) # e.j. UETU538323-9
    seal_number = models.CharField(db_column='Seal_Number', max_length=50) # e.j. 80723
    total_packages = models.CharField(db_column='Total_Packages', max_length=10) # e.j. 1x40 HQ
    commodity = models.CharField(db_column='Commodity', max_length=100) # e.j. Carga General
    hs_code = models.CharField(db_column='HS_Code', max_length=25)
    pickup_dpto = models.CharField(db_column='Pickup_Dpto.', max_length=75)
    pickup_ref = models.IntegerField(db_column='Pickup_Ref', blank=True, null=True)
    products = models.CharField(db_column='Products', max_length=10000)

    # Weight and Size Information
    tare = models.CharField(db_column='Tare', max_length=20)
    gross_weight = models.CharField(db_column='Gross_Weight', max_length=15)
    size = models.CharField(db_column='Container_Size', max_length=10) # e.j. CB3/M3
    net_weight = models.CharField(db_column='Net_weight', max_length=20)

    # Payment Information
    client_name = models.CharField(db_column='Client_Name', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    charge_code = models.CharField(db_column='Charge_Code', max_length=75)
    payment = models.CharField(db_column='Payment', max_length=20)
    rateper = models.CharField(db_column='Rateper', max_length=20, blank=True, null=True)
    freightcharges = models.CharField(db_column='FreightCharges', max_length=20)
    prepaid = models.CharField(db_column='Prepaid', max_length=10)
    collect = models.CharField(db_column='Collect', max_length=20, blank=True, null=True)

    # Shipper Information
    shipper_name = models.CharField(db_column='Shipper_Name', max_length=100)
    shipper_address = models.CharField(db_column='Shipper_Address', max_length=75)
    shipper_city = models.CharField(db_column='Shipper_City', max_length=75)
    shipper_state = models.CharField(db_column='Shipper_State/Province', max_length= 50)
    shipper_country = models.CharField(db_column='Shipper_Country', max_length=75)
    shipper_email = models.CharField(db_column='Shipper_Email', max_length=50)

    # Consignee Information
    consignee_name = models.CharField(db_column='Consignee_Name', max_length=100)
    consignee_address = models.CharField(db_column='Consignee_Address', max_length= 50)
    consignee_city = models.CharField(db_column='Consignee_City', max_length= 50)
    consignee_state = models.CharField(db_column='Consignee_State/Province', max_length= 50)
    consignee_country = models.CharField(db_column='Consignee_Country', max_length= 50)
    consignee_email = models.CharField(db_column='Consignee_Email', max_length=50)

    # Notify Information - Go over with Ricky
    notify_name = models.CharField(db_column='Notify_Name', max_length=100)
    notify_address = models.CharField(db_column='Notify_Address', max_length= 50)
    notify_city = models.CharField(db_column='Notify_City', max_length= 50)
    notify_state = models.CharField(db_column='Notify_State/Province', max_length= 50)
    notify_country = models.CharField(db_column='Notify_Country', max_length= 50)
    notify_email = models.CharField(db_column='Notify_Email', max_length=50)