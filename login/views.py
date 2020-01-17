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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

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
	return render(request, 'login/round1.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })


@login_required
def round2(request):
	date = Date.objects.get(pk=3)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })


@login_required
def round3(request):
	date = Date.objects.get(pk=4)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })


@login_required
def round4(request):
	date = Date.objects.get(pk=5)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })	 		 		


@login_required
def round5(request):
	date = Date.objects.get(pk=6)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })	


@login_required
def round6(request):
	date = Date.objects.get(pk=7)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })	


@login_required
def round7(request):
	date = Date.objects.get(pk=8)
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
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })	

@login_required
def round8(request):
	date = Date.objects.get(pk=9)
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
					user.profile.Enigma += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price8)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price8)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price8)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
					user.profile.money+=amount*(company_name.price8)
					user.profile.save()
													

	all_company = company.objects.all()
	return render(request, 'login/round8.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })

@login_required
def round9(request):
	date = Date.objects.get(pk=10)
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
					user.profile.Enigma += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price9)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price9)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price9)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
					user.profile.money+=amount*(company_name.price9)
					user.profile.save()
													

	all_company = company.objects.all()
	return render(request, 'login/round9.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })


@login_required
def round10(request):
	date = Date.objects.get(pk=11)
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
					user.profile.Enigma += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Enigma - amount > error:
					user.profile.Enigma-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()

		elif company_str == 'Tec Solutions':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Tec += amount/(company_name.price10)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Tec - amount > error:
					user.profile.Tec-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()

		elif company_str == 'GAAP Cinemas':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.GAAP += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.GAAP - amount > error:
					user.profile.GAAP-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()
		
		elif company_str == 'ALPHA Leisure Limited':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.ALPHA += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.ALPHA - amount > error:
					user.profile.ALPHA-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()	

		elif company_str == 'LAXMI Bank Ltd.':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.LAXMI += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.LAXMI - amount > error:
					user.profile.LAXMI-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()		

		elif company_str == 'Punjab National Bank':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Punjab += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Punjab - amount > error:
					user.profile.Punjab-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()

		elif company_str == 'Lifepoint Hospitals':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.Lifepoint += amount/(company_name.price10)
					user.profile.money -=  amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.Lifepoint - amount > error:
					user.profile.Lifepoint-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()

		elif company_str == 'RIGHT Laboratories':
			if opr == 'buy':
				if user.profile.money - amount > error:
					user.profile.RIGHT += amount/(company_name.price10)
					user.profile.money -= amount
					user.profile.save()
			elif opr == 'sell':
				if user.profile.RIGHT - amount > error:
					user.profile.RIGHT-=amount
					user.profile.money+=amount*(company_name.price10)
					user.profile.save()
													

	all_company = company.objects.all()
	return render(request, 'login/round10.html', { 
			'user': user,
			'companys': all_company,
			'date': date,
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })

@login_required
def finish(request):
	user = request.user		
	if request.method == 'POST':
		user.profile.feedback = str(request.POST['message'])
		user.profile.save()
		all_company = company.objects.all()
		return render(request, 'login/finish.html', { 
			'user': user,
			'companys': all_company,
			'message': "Feedback Submitted Successfully!",
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })
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

	all_company = company.objects.all()
	return render(request, 'login/finish.html', { 
			'user': user,
			'companys': all_company,
			'tec0': (company.objects.get(pk=2)).price0,
			'tec1': (company.objects.get(pk=2)).price1,
			'tec2': (company.objects.get(pk=2)).price2,
			'tec3': (company.objects.get(pk=2)).price3,
			'tec4': (company.objects.get(pk=2)).price4,
			'tec5': (company.objects.get(pk=2)).price5,
			'tec6': (company.objects.get(pk=2)).price6,
			'tec7': (company.objects.get(pk=2)).price7,
			'tec8': (company.objects.get(pk=2)).price8,
			'tec9': (company.objects.get(pk=2)).price9,
			'tec10': (company.objects.get(pk=2)).price10,
			'en0': (company.objects.get(pk=1)).price0,
			'en1': (company.objects.get(pk=1)).price1,
			'en2': (company.objects.get(pk=1)).price2,
			'en3': (company.objects.get(pk=1)).price3,
			'en4': (company.objects.get(pk=1)).price4,
			'en5': (company.objects.get(pk=1)).price5,
			'en6': (company.objects.get(pk=1)).price6,
			'en7': (company.objects.get(pk=1)).price7,
			'en8': (company.objects.get(pk=1)).price8,
			'en9': (company.objects.get(pk=1)).price9,
			'en10': (company.objects.get(pk=1)).price10,
			'gaa0': (company.objects.get(pk=3)).price0,
			'gaa1': (company.objects.get(pk=3)).price1,
			'gaa2': (company.objects.get(pk=3)).price2,
			'gaa3': (company.objects.get(pk=3)).price3,
			'gaa4': (company.objects.get(pk=3)).price4,
			'gaa5': (company.objects.get(pk=3)).price5,
			'gaa6': (company.objects.get(pk=3)).price6,
			'gaa7': (company.objects.get(pk=3)).price7,
			'gaa8': (company.objects.get(pk=3)).price8,
			'gaa9': (company.objects.get(pk=3)).price9,
			'gaa10': (company.objects.get(pk=3)).price10,
			'alp0': (company.objects.get(pk=4)).price0,
			'alp1': (company.objects.get(pk=4)).price1,
			'alp2': (company.objects.get(pk=4)).price2,
			'alp3': (company.objects.get(pk=4)).price3,
			'alp4': (company.objects.get(pk=4)).price4,
			'alp5': (company.objects.get(pk=4)).price5,
			'alp6': (company.objects.get(pk=4)).price6,
			'alp7': (company.objects.get(pk=4)).price7,
			'alp8': (company.objects.get(pk=4)).price8,
			'alp9': (company.objects.get(pk=4)).price9,
			'alp10': (company.objects.get(pk=4)).price10,
			'lax0': (company.objects.get(pk=5)).price0,
			'lax1': (company.objects.get(pk=5)).price1,
			'lax2': (company.objects.get(pk=5)).price2,
			'lax3': (company.objects.get(pk=5)).price3,
			'lax4': (company.objects.get(pk=5)).price4,
			'lax5': (company.objects.get(pk=5)).price5,
			'lax6': (company.objects.get(pk=5)).price6,
			'lax7': (company.objects.get(pk=5)).price7,
			'lax8': (company.objects.get(pk=5)).price8,
			'lax9': (company.objects.get(pk=5)).price9,
			'lax10': (company.objects.get(pk=5)).price10,
			'pnb0': (company.objects.get(pk=6)).price0,
			'pnb1': (company.objects.get(pk=6)).price1,
			'pnb2': (company.objects.get(pk=6)).price2,
			'pnb3': (company.objects.get(pk=6)).price3,
			'pnb4': (company.objects.get(pk=6)).price4,
			'pnb5': (company.objects.get(pk=6)).price5,
			'pnb6': (company.objects.get(pk=6)).price6,
			'pnb7': (company.objects.get(pk=6)).price7,
			'pnb8': (company.objects.get(pk=6)).price8,
			'pnb9': (company.objects.get(pk=6)).price9,
			'pnb10': (company.objects.get(pk=6)).price10,
			'lif0': (company.objects.get(pk=7)).price0,
			'lif1': (company.objects.get(pk=7)).price1,
			'lif2': (company.objects.get(pk=7)).price2,
			'lif3': (company.objects.get(pk=7)).price3,
			'lif4': (company.objects.get(pk=7)).price4,
			'lif5': (company.objects.get(pk=7)).price5,
			'lif6': (company.objects.get(pk=7)).price6,
			'lif7': (company.objects.get(pk=7)).price7,
			'lif8': (company.objects.get(pk=7)).price8,
			'lif9': (company.objects.get(pk=7)).price9,
			'lif10': (company.objects.get(pk=7)).price10,
			'rig0': (company.objects.get(pk=8)).price0,
			'rig1': (company.objects.get(pk=8)).price1,
			'rig2': (company.objects.get(pk=8)).price2,
			'rig3': (company.objects.get(pk=8)).price3,
			'rig4': (company.objects.get(pk=8)).price4,
			'rig5': (company.objects.get(pk=8)).price5,
			'rig6': (company.objects.get(pk=8)).price6,
			'rig7': (company.objects.get(pk=8)).price7,
			'rig8': (company.objects.get(pk=8)).price8,
			'rig9': (company.objects.get(pk=8)).price9,
			'rig10': (company.objects.get(pk=8)).price10,

		 })