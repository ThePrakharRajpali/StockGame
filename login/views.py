from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import company, Date

@login_required
def site(request):
	date = Date.objects.get(pk=1)
	user = request.user
	if request.method == 'POST':
		error = -0.000000001
		company_str = str(company.objects.get(pk=request.POST['company_id']))
		company_name = company.objects.get(pk=request.POST['company_id'])
		opr = str(request.POST['what'])
		amount = float(request.POST['amount'])

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()
													

	all_company = company.objects.all()
	return render(request, 'login/site.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
		 })					


@login_required
def detail(request, id):
	c_name = str(company.objects.get(pk=id))  
	if c_name == 'Enigma Limited':
		return render(request, 'login/Enigma.html', {'title': 'Enigma Limited'})
	elif c_name == 'Tec Solutions':
		return render(request, 'login/Tec.html', {'title': 'Tec Solutions'})	
	elif c_name == 'GAAP Cinemas':
		return render(request, 'login/GAAP.html', {'title': 'GAAP Cinemas'})
	elif c_name == 'ALPHA Leisure Limited':
		return render(request, 'login/ALPHA.html', {'title': 'ALPHA Leisure Limited'})
	elif c_name == 'LAXMI Bank Ltd.':
		return render(request, 'login/LAXMI.html', {'title': 'LAXMI Bank Ltd.'})
	elif c_name == 'Punjab National Bank':
		return render(request, 'login/Punjab.html', {'title': 'Punjab National Bank'})
	elif c_name == 'Lifepoint Hospitals':
		return render(request, 'login/Lifepoint.html', {'title': 'Lifepoint Hospitals'})	
	elif c_name == 'RIGHT Laboratories':
		return render(request, 'login/RIGHT.html', {'title': 'RIGHT Laboratories'})
						

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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price1)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price1)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price1)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price2)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price2)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price2)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price2)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price3)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price3)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price3)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price3)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price4)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price4)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price4)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price4)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price5)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price5)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price5)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price5)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price6)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price6)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price6)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price6)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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

		if company_str == 'Enigma Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Enigma += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price7)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price7)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price7)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price7)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
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
	user.profile.money+=user.profile.Enigma*comp.price0
	comp = company.objects.get(pk=2)
	user.profile.money+=user.profile.Tec*comp.price0
	comp = company.objects.get(pk=3)
	user.profile.money+=user.profile.GAAP*comp.price0
	comp = company.objects.get(pk=4)
	user.profile.money+=user.profile.ALPHA*comp.price0
	comp = company.objects.get(pk=5)
	user.profile.money+=user.profile.LAXMI*comp.price0
	comp = company.objects.get(pk=6)
	user.profile.money+=user.profile.Punjab*comp.price0
	comp = company.objects.get(pk=7)
	user.profile.money+=user.profile.Lifepoint*comp.price0
	comp = company.objects.get(pk=8)
	user.profile.money+=user.profile.RIGHT*comp.price0
	
	user.profile.Enigma=0
	user.profile.RIGHT=0
	user.profile.ALPHA=0
	user.profile.Tec=0
	user.profile.GAAP=0
	user.profile.LAXMI=0
	user.profile.Punjab=0
	user.profile.Lifepoint=0
	user.profile.save()

	return render(request, 'login/finish.html', { 'user': user })