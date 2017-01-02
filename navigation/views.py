# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from navigation.models import Domain

@login_required
def list (request):
	domains = Domain.objects.all()
	
	return render(
        request,
        'navigation.html',
    )
