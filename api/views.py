from django.shortcuts import render
from django.http import HttpResponse
from FSP.settings import STATICFILES_DIRS
import json
# Create your views here.

def home(request):
    with open(f'{STATICFILES_DIRS[0]}/solution.json', 'r') as file:
        json_data = json.load(file)
    return render(request, 'path.html', {"list_of_dict": json_data})