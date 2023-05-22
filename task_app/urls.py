from django.urls import path
from task_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('create', create_task, name='crate_task'),
    path('delete/<str:id_task>', delete_task, name='delete_task'),
    path('edit/<str:id_task>', edit_task, name='edit_task')

]