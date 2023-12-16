from django.urls import path
from . import views

urlpatterns=[
   path('add/', views.AddCarView.as_view(), name='add_car'),
   path('edit/<int:pk>', views.EditCarView.as_view(), name='edit_car'),
   path('delete/<int:pk>', views.DeleteCarView.as_view(), name='delete_car'),
   path("details/<int:pk>/", views.CarDetails.as_view() , name="details"),
   path("buy/<int:pk>/", views.buy , name="buy"),
]