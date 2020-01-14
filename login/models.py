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
	Apple = models.FloatField(default=0)
	Amazon = models.FloatField(default=0)
	Microsoft = models.FloatField(default=0)
	Alphabet = models.FloatField(default=0)
	Berkshire = models.FloatField(default=0)
	Facebook = models.FloatField(default=0)
	Tencent = models.FloatField(default=0)
	Alibaba = models.FloatField(default=0)
	Johnson = models.FloatField(default=0)
	JPMorgan = models.FloatField(default=0)


	def __str__(self):
		return f'{self.user.username}'

	def save(self, *args, **kwargs):
		self.money = round(self.money, 4)
		self.Apple = round(self.Apple, 4)
		self.Amazon = round(self.Amazon, 4)
		self.Microsoft = round(self.Microsoft, 4)
		self.Alphabet = round(self.Alphabet, 4)
		self.Berkshire = round(self.Berkshire, 4)
		self.Facebook = round(self.Facebook, 4)
		self.Tencent = round(self.Tencent, 4)
		self.Alibaba = round(self.Alibaba, 4)
		self.Johnson = round(self.Johnson, 4)
		self.JPMorgan = round(self.JPMorgan, 4)
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