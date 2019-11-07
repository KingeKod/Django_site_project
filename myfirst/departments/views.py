from django.shortcuts import render
from . import models
from django_pivot.pivot import pivot
from .models import TechDepartment, DepartmentOffice, Indicate #,TechDepartment, Indicate

#@api_view(['GET'])
def output(request):
	indicators = []
	indicators_2 = []
	date_from = "2019-01-01"
	date_to = "2019-04-01"
	
	if request.GET.get('from',''):
		date_from = request.GET.get('from','')
	if request.GET.get('to',''):
		date_to = request.GET.get('to','')
	sort_date = DepartmentOffice.objects.all().filter(date__range=[date_from,date_to])
	piv=pivot(sort_date, 'office__technical_department','id_group__indicator', 'value')

	for dict in piv:
		for k,v in dict.items():
			indicators.append(v)
		indicators_2.append(indicators)	
		indicators = []
	
	table = DepartmentOffice.objects.all().order_by('office', 'date')
	return render(request, 'departments/index.html', {'table':table, 'indicators':[indicators_2], 'from':date_from, 'to':date_to})
