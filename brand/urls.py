from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddBrandView.as_view(), name='add_brand'),
    path('edit/<int:pk>', views.EditBrandView.as_view(), name='edit_brand'),
    path('delete/<int:pk>', views.DeleteBrandView.as_view(), name='delete_brand'),
]