from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('debtors/', views.DebtorList.as_view(), name='debtors_list'),
    path('debtors/<int:debtor_id>/', views.debtors_detail, name='detail'),
    path('debtors/create/', views.DebtorCreate.as_view(), name='debtors_create'),
    path('debtors/<int:pk>/update', views.DebtorUpdate.as_view(), name='debtors_update'),
    path('debtors/<int:pk>/delete', views.DebtorDelete.as_view(), name='debtors_delete'),
    path('debtors/<int:debtor_id>/add_payment/', views.add_payment, name='add_payment'),
    path('debtors/<int:debtor_id>/assoc_insurance/<int:insurance_id>/', views.assoc_insurance, name='assoc_insurance'),
    path('insurance/', views.InsuranceList.as_view(), name='insurance_index'),
    path('insurance/create/', views.InsuranceCreate.as_view(), name='insurance_create'),
    path('insurance/<int:pk>/delete/', views.InsuranceDelete.as_view(), name='insurance_delete'),
]