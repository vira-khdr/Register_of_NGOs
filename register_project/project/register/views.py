from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Commerce_Chambers
import add_organization

def index(request):
    return render_to_response('index.html')

def page_commerse_chambers(request):
    return render_to_response('add_commerce_chambers.html')

@csrf_exempt
def add_commerse_chambers(request):
    if request.method == "POST":
        add_organization.add_commerce_chambers(request.POST)

    return render_to_response('index.html')