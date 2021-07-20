from django.db import models
from django.utils.html import mark_safe

# Banners
class Banners(models.Model):
	img=models.ImageField(upload_to="banners/")
	alt_text=models.CharField(max_length=150)

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Create your models here.
class Service(models.Model):
	title=models.CharField(max_length=150)
	detail=models.TextField()
	img=models.ImageField(upload_to="services/",null=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Pages
class Page(models.Model):
	title=models.CharField(max_length=200)
	detail=models.TextField()

	def __str__(self):
		return self.title

# FAQ
class Faq(models.Model):
	quest=models.TextField()
	ans=models.TextField()

	def __str__(self):
		return self.quest

# Enquiry Model
class Enquiry(models.Model):
	full_name=models.CharField(max_length=150)
	email=models.CharField(max_length=150)
	detail=models.TextField()
	send_time=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.full_name

# Gallery Model
class Gallery(models.Model):
	title=models.CharField(max_length=150)
	detail=models.TextField()
	img=models.ImageField(upload_to="gallery/",null=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Gallery Images
class GalleryImage(models.Model):
	gallery=models.ForeignKey(Gallery, on_delete=models.CASCADE,null=True)
	alt_text=models.CharField(max_length=150)
	img=models.ImageField(upload_to="gallery_imgs/",null=True)

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))
