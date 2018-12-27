from django.urls import path

from sjp import views

app_name = 'sjp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('purchases/<int:pk>/', views.PurchaseDetail.as_view(), name='purchase-detail'),
    path('purchases/', views.PurchaseList.as_view(), name='purchase-list'),
    path('joint_purchases/<int:pk>/', views.JointPurchaseDetail.as_view(), name='joint-purchase-detail'),
    path('joint_purchases/', views.JointPurchaseList.as_view(), name='joint-purchase-list'),
]
