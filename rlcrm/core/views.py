from django.shortcuts import render

# request is a paramater that contains information about the browser(post or get request)
def index(request):
    return render(request, 'core/index.html')
