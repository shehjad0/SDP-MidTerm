from django.urls import path
from . import views

urlpatterns=[
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
    path("sign_in/", views.SignIn.as_view(), name="sign_in"),
    path("sign_out/", views.SignOut.as_view(), name="sign_out"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
]