from django.shortcuts import render

def index(request):
    apps = ['admin', 'polls', 'blog', 'movies', 'accounts', 'api/countries']
    return render(request, 'index.html', {'apps': apps})