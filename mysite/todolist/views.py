from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


class UserLogin(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")


class Index(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(is_done=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_detail.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "task_text", "is_done"]
    template_name = "task_create.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "task_text", "is_done"]
    template_name = "task_create.html"
    success_url = reverse_lazy("index")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("index")
    template_name = "task_delete.html"


class RegistrationForm(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationForm, self).form_valid(form)
