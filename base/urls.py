from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView,  RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('todo/login/', CustomLoginView.as_view(), name='login'),
    path('todo/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('todo/register/', RegisterPage.as_view(), name='register'),
    path('todo/', TaskList.as_view(), name='tasks'),
    path('todo/task/<int:pk>/',  TaskDetail.as_view(), name='task'),
    path('todo/task-create/', TaskCreate.as_view(), name='task-create'),
    path('todo/task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('todo/task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete')
]