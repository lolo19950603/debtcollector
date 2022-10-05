from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('debtors/', views.DebtorList.as_view(), name='debtors_list'),
    path('debtors/<int:pk>/', views.DebtorDetail.as_view(), name='debtors_detail'),
    path('debtors/create/', views.DebtorCreate.as_view(), name='debtors_create'),
    path('debtors/<int:pk>/update', views.DebtorUpdate.as_view(), name='debtors_update'),
    path('debtors/<int:pk>/delete', views.DebtorDelete.as_view(), name='debtors_delete')
]