from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import SignupForm
from urllib.parse import unquote
from urllib.parse import urlparse
from urllib.parse import parse_qs


def profile_view(request):
    # print(request.body.decode(encoding='UTF-8'))
    try:
        params = request.body.decode(encoding='UTF-8').split('&')
        username = params[0].split('=')[1]
        email = params[1].split('=')[1]
        request.user.username = unquote(username)
        request.user.email = unquote(email)
        request.user.save()
    except:
        pass

    context = {}
    return render(request, 'account_profile.html', context)


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['profile_form'] = ProfileCreateForm(self.request.POST or None)
    #     print(context)
    #     return context
    #
    # def form_valid(self, form):
    #     profile_form = ProfileCreateForm(self.request.POST)
    #     if profile_form.is_valid():
    #         self.object = form.save()
    #         profile = profile_form.save(commit=False)
    #         profile.user = self.object
    #         profile.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_invalid(self, form):
    #     # same as above
    #     print('form is invalid')
    #     return super().form_invalid(form)


def check_username(request):
    print('hit')
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:#e76f51;'>This name is already taken<div>")
    elif username == '':
        return HttpResponse('')
    else:
        return HttpResponse("<div style='color:#2a9d8f;'>This name is available<div>")


def test(request):
    payload = request.GET.get('payload')

    return HttpResponse(f'<div class="card">you chose a {payload}</div>')


def profile_edit_view(request):
    return render(request, 'account_profile_edit.html', {})
