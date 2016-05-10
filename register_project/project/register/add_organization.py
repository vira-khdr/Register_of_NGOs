from . models import Commerce_Chambers, Document, Address, Certificate
from datetime import date
import random

def add_commerce_chambers(post_data):
    #commerce chamber info
    ch_type = post_data.__getitem__('ch_type')
    oper_type = post_data.__getitem__('oper_type')
    #register_number == null
    org_full_name = post_data.__getitem__('org_full_name')
    org_location = post_data.__getitem__('org_location')
    org_goal = post_data.__getitem__('org_goal')
    registrator_name = "Vira Rodionova"

    #document info
    doc_name = post_data.__getitem__('doc_name')
    doc_num = post_data.__getitem__('doc_num')
    doc_date = post_data.__getitem__('doc_date')
    doc_registrator = post_data.__getitem__('doc_registrator')

    #address info
    addr_region = post_data.__getitem__('addr_region')
    addr_area = post_data.__getitem__('addr_area')
    addr_city = post_data.__getitem__('addr_city')
    addr_adderss = post_data.__getitem__('addr_adderss')
    addr_post_index = post_data.__getitem__('addr_post_index')
    addr_phone = post_data.__getitem__('addr_phone')

    #certificate info
    random.seed()
    cert_num = str(random.randint(1000000000, 10000000000))

    #add commerce chamber
    address = Address.objects.create(region=addr_region, area=addr_area, city=addr_city, address=addr_adderss,
                                     post_index=addr_post_index, phone=addr_phone)
    document = Document.objects.create(name=doc_name, number=doc_num, date=doc_date, issued_by=doc_registrator)
    certificate = Certificate.objects.create(number=cert_num, date=date.today())

    Commerce_Chambers.objects.create(ch_type=ch_type, oper_type=oper_type, name_full=org_full_name, location=org_location,
                                     goal=org_goal, registrator_name=registrator_name,
                                     cert=certificate, doc=document, address=address)

    print Commerce_Chambers.objects.all()