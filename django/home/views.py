from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # any other context you need
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()        # create the user
            login(request, user)      # log them in immediately
            return redirect('/')      # send them to home (or use 'home' URL name)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})