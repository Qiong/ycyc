from django.db import models

# Create your models here.

class NewsLink(models.Model):

	startup = models.ForeignKey(Startup)
	pub_date = models.DateField(verbose_name='Date Published')

class Startup(models.Model):

	tags = models.ManyToManyField(Tag)
	name = models.CharField(max_length=31,db_index=True)
	slug = models.SlugField(max_length=31, unique=True,help_text='A label for URl config')
	founded_date = models.DateField(verbose_name='Date Founded')

	def __str__(self):
        return self.name

class Tag(models.Model):

	name = models.CharField(max_length = 31, unique = True)
	slug = models.SlugField(max_length = 31, unique = True, help_text = 'A label for URL config.')

	def __str__(self):
        return self.name
