from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.employee_form,name='employee_insert'),# get and post  for insert operation
    path('<int:id>/',views.employee_form,name='employee_update'),# get and post  for update operation
    path('delete/<int:id>',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list')## get and post  for retrive and display operation
]