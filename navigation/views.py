# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from navigation.models import Domain

@login_required
def list (request):
	domains = []
	RecordDic = {}
	D = Domain.objects.all()
	index = 0
	for domain in D:
		RecordDic['product'] = domain.product
		RecordDic['abbr']    = domain.abbr
		RecordDic['domain']  = domain.domain
		RecordDic['record']  = domain.record
		domains.append(RecordDic)
	return render(
        request,
        'navigation.html',
        {
        	'domains':domains
        }
    )
