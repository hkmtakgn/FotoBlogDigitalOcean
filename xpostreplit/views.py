from django.shortcuts import render

# Create your views here.


def home_views(request):
    context = dict()
    return render(request, "main/xpost-home.html", context)
