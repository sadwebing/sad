# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def list(request):
    return render(
        request,
        'navigation.html',
    )
