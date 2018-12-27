from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import User, Purchase, JointPurchase

# Create your views here.


class Index(TemplateView):
    template_name = 'sjp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['purchases'] = Purchase.objects.filter(id_author=user)
        return context


class PurchaseList(ListView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase


class JointPurchaseList(ListView):
    model = JointPurchase


class JointPurchaseDetail(DetailView):
    model = JointPurchase


class UserList(ListView):
    model = User


class UserDetail(DetailView):
    context_object_name = 'myuser'
    model = User