from django.contrib import admin
from django.urls import path
from .views import Index, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLogin, RegistrationForm


urlpatterns = [
    # path("login/", UserLogin.as_view(), name="login"),
    # path('logout/', UserLogout.as_view(), name="logout"),
    path("register/", RegistrationForm.as_view(), name="register"),
    path("", Index.as_view(), name="index"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task_detail"),
    path("task/create/", TaskCreate.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdate.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDelete.as_view(), name="task_delete"),

]
