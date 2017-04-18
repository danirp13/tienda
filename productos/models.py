
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Marca(models.Model):
    """ Categorias para clasificar los zapatos """
    name = models.CharField(max_length=50)
    def __str__(self):             
        return self.name


class Zapato(models.Model):
	"""Fotos de los zapatos"""
	marca=models.ForeignKey(Marca,null=True,blank=True)
	title=models.CharField(max_length=50,default='No title')
	photo=models.ImageField(upload_to='photos/')
	pub_date=models.DateField(auto_now_add=True)
	favorite=models.BooleanField(default=False)
	comment=models.CharField(max_length=200,blank=True) 
	def get_absolute_url(self):
		return reverse ('zapato-list')
	def __str__(self):
		return self.title       