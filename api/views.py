from django.shortcuts import render
from django.http import HttpResponse
from FSP.settings import STATICFILES_DIRS
import json
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def path(reqest, path_name):
    if path_name == "python" or path_name == "git":
        with open(f'{STATICFILES_DIRS[0]}/{path_name}.json', 'r') as file:
            json_data = json.load(file)
        return render(reqest, "path.html", {"list_of_dict": json_data})
    else:
        return HttpResponse("<h1>404 Page Not Found</h1>")