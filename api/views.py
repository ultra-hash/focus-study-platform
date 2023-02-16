from django.shortcuts import render
from django.http import HttpResponse
from FSP.settings import STATICFILES_DIRS
import json
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def path(reqest, path_name):
    path_list = ['git', 'python', 'django', 'djangorestframework', 'dsawithpython', 'pandas', 'java']
    if path_name in path_list:
        with open(f'{STATICFILES_DIRS[0]}/{path_name}.json', 'r') as file:
            json_data = json.load(file)

        name_of_the_path = json_data['path_name']
        videos_data = json_data['data']
        return render(reqest, "path.html", {"list_of_videos": videos_data, "name_of_the_path": name_of_the_path, "videos_length_plus_1": len(videos_data)})
    else:
        return HttpResponse("<h1>404 Page Not Found</h1>")