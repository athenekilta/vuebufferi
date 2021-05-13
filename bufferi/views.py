from django.shortcuts import render


def index(request):
    """Serves Vue frontend"""
    return render(request, template_name="index.html")

