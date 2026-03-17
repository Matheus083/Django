from django.shortcuts import render


# Create your views here.
def blog(request):
    context = {'text': 'Hello! We are in the BLOG.'}
    return render(
        request,
        'blog/index.html',
        context
    )


def example(request):
    context = {
        'text': 'Hello! We are in the EXAMPLE.', 
        'title': 'You are my page.'
                      }
    return render(
        request,
        'blog/example.html',
        context
    )
