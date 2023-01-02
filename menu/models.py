from django.db import models

# Create your models here.


class Menu(models.Model):
	'''Simple Menu Example'''
	title = models.CharField(max_length=128)

	def __str__(self):
		return self.title


class MenuItem(models.Model):
	'''Items of Menu'''
	title = models.CharField(max_length=128)

	# Relations
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
		related_name='menu_items')
	parent = models.ForeignKey('self', on_delete=models.CASCADE,
		related_name='child_items', null=True, blank=True)

	def __str__(self):
		return self.title