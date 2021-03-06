from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=63)
	slug = models.SlugField(max_length=63,help_text='A label for URL config', unique_for_month='pub_date')

	text = models.TextField()
	pub_date = models.DateField(auto_now_add=True,verbose_name='Date Published')
	tags = models.ManyToManyField(Tag,related_name='blog_posts')
	startups = models.ManyToManyField(Startup,related_name='blog_posts')