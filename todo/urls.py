from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('add', views.add , name = 'add'),
    path('complet/<todo_id>', views.dodo , name = 'end'),
    path('delete', views.delete_text , name = 'delete'),
    path('delete_all', views.delete_all , name = 'delete_all')

]