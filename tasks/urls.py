from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register', views.register, name='register'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("create-task/", views.create_task, name="create_task"),
    path("tasks/", views.task_list, name="task_list"),
    path("users/", views.user_list, name="user_list"),
    path("tasks/<int:pk>/", views.task_detail, name="task_detail"),
    path("tasks/edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("tasks/delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("users/<int:pk>/", views.user_detail, name="user_detail"),
    path("users/<int:pk>/edit/", views.user_edit, name="user_edit"),
    path("users/<int:pk>/delete/", views.user_delete, name="user_delete"),
    path("tasks/completed/", views.completed_tasks, name="completed_tasks"),

    # REST APIs
    path("api/login/", views.LoginAPIView.as_view(), name="api_login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/my-tasks/", views.UserTaskListAPIView.as_view(), name="api_my_tasks"),
    path("api/tasks/<int:pk>/update/", views.TaskUpdateAPIView.as_view(), name="api_task_update"),
    path("api/tasks/completed/", views.CompletedTaskListAPIView.as_view(), name="api_completed_tasks")
]
