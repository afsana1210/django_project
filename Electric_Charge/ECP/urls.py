from django.urls import path
from .view import USERS

urlpatterns=[
    # path('',views.index,name='index'),
    # path('create',views.CreateMyModelView.as_view(),name='create'),
    path('signup/',views.signup_view ,name='signup'),
]
