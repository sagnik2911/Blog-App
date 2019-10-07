from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author': 'KalpakSeal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 6, 2019'
    },
    {
        'author': 'SagnikGhosh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 5, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
    # return HttpResponse('<h1>Blog About</h1>')