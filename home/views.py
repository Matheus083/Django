from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'text': 'Python is a beautiful language!!!'}
    return render(request, 'home/index.html', context)
