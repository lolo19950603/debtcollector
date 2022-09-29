from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('debtors/', views.debtors_index, name='index'),
    path('debtors/<int:debtor_id>/', views.debtors_detail, name='detail')
]