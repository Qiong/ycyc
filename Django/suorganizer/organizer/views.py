from django.shortcuts import render

# Create your views here.

class Tag(models.Model):
	name = models.CharField(max_length=31)
	slug = models.SlugField(max_length=31)

class Startup(models.Model):
	name = models.CharField(max_length=31)
	slug = models.SlugField(max_length=31)
	description = models.TextField()
	founded_date = models.DateField()
	contact = models.EmailField(max_length=254)
	website = models.URLField(max_length=255)

class NewsLink(models.Model):
	title = models.CharField(max_length=63)
	pub_date = models.DateField()
	link = models.URLField(max_length=255)
