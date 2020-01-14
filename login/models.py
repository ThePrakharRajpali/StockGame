from django.db import models
from django.contrib.auth.models import User


class company(models.Model):
	company_name = models.CharField(max_length=50)
	sector = models.CharField(max_length=25, default="max cap")
	cat = models.CharField(max_length=25, default="tec")
	price0 = models.FloatField()
	price1 = models.FloatField()
	price2 = models.FloatField()
	price3 = models.FloatField()
	price4 = models.FloatField()
	price5 = models.FloatField()
	price6 = models.FloatField()
	price7 = models.FloatField()
	

	def __str__(self):
		return self.company_name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)		
	money = models.FloatField(default=10000)
	Enigma = models.FloatField(default=0)
	Tec = models.FloatField(default=0)
	GAAP = models.FloatField(default=0)
	ALPHA = models.FloatField(default=0)
	LAXMI = models.FloatField(default=0)
	Punjab = models.FloatField(default=0)
	Lifepoint = models.FloatField(default=0)
	RIGHT = models.FloatField(default=0)


	def __str__(self):
		return f'{self.user.username}'

	def save(self, *args, **kwargs):
		self.money = round(self.money, 4)
		self.Enigma = round(self.Enigma, 4)
		self.Tec = round(self.Tec, 4)
		self.GAAP = round(self.GAAP, 4)
		self.ALPHA = round(self.ALPHA, 4)
		self.LAXMI = round(self.LAXMI, 4)
		self.Punjab = round(self.Punjab, 4)
		self.Lifepoint = round(self.Lifepoint, 4)
		self.RIGHT = round(self.RIGHT, 4)

		super(Profile, self).save(*args, **kwargs)	

class Date(models.Model):
	month = models.CharField(max_length=3)
	year = models.IntegerField(default=2019)
	num = models.IntegerField(default=0)
	day = models.IntegerField(default=0)
	hour = models.IntegerField(default=0)
	minute = models.IntegerField(default=0)


	def __str__(self):
		return str(self.num)		