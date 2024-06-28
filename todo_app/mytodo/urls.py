from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
     path("", mytodo.index,name="index"),
     path("add/", mytodo.add,name="add"),
     path("updata_task_complete/", mytodo.update_task_complete,name="update_task_complete"),
     path("edit/<int:task_id>/", mytodo.edit, name='edit'),
     path("delete/<int:task_id>/", mytodo.delete, name='delete'),
]
