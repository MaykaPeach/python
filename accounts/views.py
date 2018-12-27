from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from . import forms


# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = 'accounts/login'
#     template_name = 'accounts/register.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)


class RegisterFormView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'
