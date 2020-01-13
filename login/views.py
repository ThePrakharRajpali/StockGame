from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import company, Date

@login_required
def site(request):
	user = request.user
	all_company = company.objects.all()
	date = Date.objects.get(pk=1)
	return render(request, 'login/site.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })


@login_required
def round1(request):
	date = Date.objects.get(pk=2)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()												

		all_company = company.objects.all()
		return render(request, 'login/round1.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round1.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })


@login_required
def round2(request):
	date = Date.objects.get(pk=3)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price2)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price2)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()												

		all_company = company.objects.all()
		return render(request, 'login/round2.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round2.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })


@login_required
def round3(request):
	date = Date.objects.get(pk=4)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price3)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price3)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()												

		all_company = company.objects.all()
		return render(request, 'login/round3.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round3.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })


@login_required
def round4(request):
	date = Date.objects.get(pk=5)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price4)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price4)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()												

		all_company = company.objects.all()
		return render(request, 'login/round4.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round4.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })		 		 		


@login_required
def round5(request):
	date = Date.objects.get(pk=6)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price5)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price5)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()											

		all_company = company.objects.all()
		return render(request, 'login/round5.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round5.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })		


@login_required
def round6(request):
	date = Date.objects.get(pk=7)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price6)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price6)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		all_company = company.objects.all()
		return render(request, 'login/round6.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round6.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })		


@login_required
def round7(request):
	date = Date.objects.get(pk=8)
	if request.method == 'POST':
		user = request.user
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Apple':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Apple += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Apple - amount > error:
					user.profile.Apple-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Amazon':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Amazon += amount/(company_name.price7)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Amazon - amount > error:
					user.profile.Amazon-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Microsoft':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Microsoft += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Microsoft - amount > error:
					user.profile.Microsoft-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()
		
		elif company_str == 'Alphabet':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alphabet += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alphabet - amount > error:
					user.profile.Alphabet-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()	

		elif company_str == 'Berkshire Hathaway':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Berkshire += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Berkshire - amount > error:
					user.profile.Berkshire-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()		

		elif company_str == 'Facebook':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Facebook += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Facebook - amount > error:
					user.profile.Facebook-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Tencent':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tencent += amount/(company_name.price7)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tencent - amount > error:
					user.profile.Tencent-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Alibaba Group':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Alibaba += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Alibaba - amount > error:
					user.profile.Alibaba-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()
		
		elif company_str == 'Johnson & Johnson':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Johnson += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Johnson - amount > error:
					user.profile.Johnson-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()	

		elif company_str == 'JPMorgan Chase':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.JPMorgan += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.JPMorgan - amount > error:
					user.profile.JPMorgan-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()												

		all_company = company.objects.all()
		return render(request, 'login/round7.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					
	else:			
		user = request.user
		all_company = company.objects.all()
		return render(request, 'login/round7.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })		


@login_required
def finish(request):
	user = request.user		
	comp = company.objects.get(pk=1)
	user.profile.money+=user.profile.Apple*comp.price0
	comp = company.objects.get(pk=2)
	user.profile.money+=user.profile.Amazon*comp.price0
	comp = company.objects.get(pk=3)
	user.profile.money+=user.profile.Microsoft*comp.price0
	comp = company.objects.get(pk=4)
	user.profile.money+=user.profile.Alphabet*comp.price0
	comp = company.objects.get(pk=5)
	user.profile.money+=user.profile.Berkshire*comp.price0
	comp = company.objects.get(pk=6)
	user.profile.money+=user.profile.Facebook*comp.price0
	comp = company.objects.get(pk=7)
	user.profile.money+=user.profile.Tencent*comp.price0
	comp = company.objects.get(pk=8)
	user.profile.money+=user.profile.Alibaba*comp.price0
	comp = company.objects.get(pk=9)
	user.profile.money+=user.profile.Johnson*comp.price0
	comp = company.objects.get(pk=10)
	user.profile.money+=user.profile.JPMorgan*comp.price0
	user.profile.Apple=0
	user.profile.Alibaba=0
	user.profile.Alphabet=0
	user.profile.Amazon=0
	user.profile.Microsoft=0
	user.profile.Berkshire=0
	user.profile.Facebook=0
	user.profile.Tencent=0
	user.profile.Johnson=0
	user.profile.JPMorgan=0
	user.profile.save()

	return render(request, 'login/finish.html', { 'user': user })