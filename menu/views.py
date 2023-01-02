from django.shortcuts import render, get_object_or_404

from .models import MenuItem
# Create your views here.


def draw_menu(request):
	'''Draw Menu'''
	return render(request, 'menu/main.html')


def draw_page(request, item_id):
	'''Draw selected page'''
	item = get_object_or_404(MenuItem, id=item_id)
	content = f'This is {item.title} page'
	context = {'content': content}
	return render(request, 'menu/page.html', context)