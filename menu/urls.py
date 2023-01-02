from django.urls import path

from . import views

urlpatterns = [
	path('', views.draw_menu, name='menu'),
	path('<int:item_id>/', views.draw_page, name='page'),
]