from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import transaction
from django.forms import ModelForm, widgets
from .models import Character, Chapter, World
from markdown2 import Markdown

# Create your views here.
class CustomLoginView(LoginView): 
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

class RegisterPage(FormView): 
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None: 
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

class CharacterList(ListView): 
    model = Character
    context_object_name = 'characters'

class CharacterDetail(DetailView): 
    model = Character
    context_object_name = 'character'
    template_name = 'base/character.html'

class CharacterUpdate(UpdateView): 
    model = Character 
    fields = "__all__"
    success_url = reverse_lazy('characters')


class CharacterDelete(DeleteView): 
    model = Character 
    fields = "__all__"
    success_url = reverse_lazy('characters')

class CharacterCreate(CreateView):
    model = Character
    fields = "__all__"
    success_url = reverse_lazy('characters')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)
    

class ChapterList(ListView): 
    model = Chapter
    context_object_name = 'chapters'

class ChapterDetail(DetailView): 
    model = Character
    context_object_name = 'chapter'
    template_name = 'base/chapter.html'

class ChapterUpdate(UpdateView): 
    model = Chapter
    fields = "__all__"
    success_url = reverse_lazy('chapters')


class ChapterDelete(DeleteView): 
    model = Chapter
    fields = "__all__"
    success_url = reverse_lazy('chapters')

class ChapterCreate(CreateView):
    model = Chapter
    fields = "__all__"
    success_url = reverse_lazy('chapters')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ChapterCreate, self).form_valid(form)
    
    
class DetailsList(ListView): 
    model = World
    context_object_name = 'details'

class DetailDetail(DetailView): 
    model = World
    context_object_name = 'detail'
    template_name = 'base/detail.html'

class DetailUpdate(UpdateView): 
    model = World
    fields = "__all__"
    success_url = reverse_lazy('details')


class DetailDelete(DeleteView): 
    model = World
    fields = "__all__"
    success_url = reverse_lazy('details')

class DetailCreate(CreateView):
    model = World
    fields = "__all__"
    success_url = reverse_lazy('details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DetailCreate, self).form_valid(form)

def home(request): 
    return render(request, 'base/landing.html')

