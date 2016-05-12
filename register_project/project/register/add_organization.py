from . models import Commerce_Chambers, Document, Address, Certificate, Leader, Limit, Party, NGO, Founder
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

def add_party(post_data):
    # commerce chamber info
    oper_type = post_data.__getitem__('oper_type')
    # register_number == null
    org_full_name = post_data.__getitem__('org_full_name')
    org_goal = post_data.__getitem__('org_goal')
    registrator_name = "Khuder Karim"

    # document info
    doc_name = post_data.__getitem__('doc_name')
    doc_num = post_data.__getitem__('doc_num')
    doc_date = post_data.__getitem__('doc_date')
    doc_registrator = post_data.__getitem__('doc_registrator')

    # address info
    addr_region = post_data.__getitem__('addr_region')
    addr_area = post_data.__getitem__('addr_area')
    addr_city = post_data.__getitem__('addr_city')
    addr_adderss = post_data.__getitem__('addr_adderss')
    addr_post_index = post_data.__getitem__('addr_post_index')
    addr_phone = post_data.__getitem__('addr_phone')

    # certificate info
    random.seed()
    cert_num = str(random.randint(1000000000, 10000000000))

    # Leader info
    lead_PIB = post_data.getlist('led_pib')
    lead_post = post_data.getlist('led_post')

    # add commerce chamber
    address = Address.objects.create(region=addr_region, area=addr_area, city=addr_city, address=addr_adderss,
                                     post_index=addr_post_index, phone=addr_phone)
    document = Document.objects.create(name=doc_name, number=doc_num, date=doc_date, issued_by=doc_registrator)
    certificate = Certificate.objects.create(number=cert_num, date=date.today())

    party = Party.objects.create(oper_type=oper_type, name_full=org_full_name,
                                 goal=org_goal, registrator_name=registrator_name,
                                 cert=certificate, doc=document, address=address)
    for i in range(len(lead_PIB)):
        leader = Leader.objects.create(PIB=lead_PIB[i], post=lead_post[i], party=party)

def add_ngo(post_data):
    #ngo info
    ngo_type = post_data.__getitem__('ch_type')
    ngo_status = post_data.__getitem__('status_type')
    legal_form = post_data.__getitem__('leg_type')
    oper_type = post_data.__getitem__('oper_type')

    # register_number == null
    org_full_name = post_data.__getitem__('org_full_name')
    org_short_name = post_data.__getitem__('org_short_name')
    org_goal = post_data.__getitem__('org_goal')
    org_direction = post_data.__getitem__('org_direction')
    registrator_name = "Topchiev Boris"

    # document info
    doc_name = post_data.__getitem__('doc_name')
    doc_num = post_data.__getitem__('doc_num')
    doc_date = post_data.__getitem__('doc_date')
    doc_registrator = post_data.__getitem__('doc_registrator')

    gov_address = post_data.__getitem__('gov_address')
    gov_phone = post_data.__getitem__('gov_phone')

    founder_PIB = post_data.getlist('nameFounder')
    founder_address = post_data.getlist('addressFounder')

    # address info
    addr_region = post_data.__getitem__('addr_region')
    addr_area = post_data.__getitem__('addr_area')
    addr_city = post_data.__getitem__('addr_city')
    addr_address = post_data.__getitem__('addr_address')
    addr_post_index = post_data.__getitem__('addr_post_index')
    addr_phone = post_data.__getitem__('addr_phone')

    # certificate info
    random.seed()
    cert_num = str(random.randint(1000000000, 10000000000))

    # Limit info
    #lim_type = post_data.__getitem__('lim_type')
    #lim_activ = post_data.__getitem__('lim_activities')
    #lim_date = post_data.__getitem__('lim_date')

    # add ngo
    address = Address.objects.create(region=addr_region, area=addr_area, city=addr_city, address=addr_address,
                                     post_index=addr_post_index, phone=addr_phone)
    document = Document.objects.create(name=doc_name, number=doc_num, date=doc_date, issued_by=doc_registrator)
    certificate = Certificate.objects.create(number=cert_num, date=date.today())

    #limit = Limit.objects.create(ch_type=lim_type, type_activities=lim_activ, date=lim_date)

    ngo = NGO.objects.create(ngo_type= ngo_type, ngo_status = ngo_status, oper_type=oper_type, legal_form = legal_form,
                             name_full=org_full_name, name_short = org_short_name, goal=org_goal, direction = org_direction,
                             registrator_name=registrator_name, cert=certificate, doc=document, address=address,
                             gov_address = gov_address, gov_phone = gov_phone)
    for i in range(len(founder_PIB)):
        founder = Founder.objects.create(PIB = founder_PIB[i], address = founder_address[i])
