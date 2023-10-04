from django.urls import path
from .views import Tasklist, TaskDetail, TaskCreate, TaskEdit, DeleteView

urlpatterns = [
    path('', Tasklist.as_view(), name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name = "task-create"),
    path('task-edit/<int:pk>/',TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete')]
