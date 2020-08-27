from django.urls import path
from ECP import views
from .views import signup_view,list_view

urlpatterns=[
    # path('',views.index,name='index'),
    # path('create',views.CreateMyModelView.as_view(),name='create'),


    path('signup/',views.signup_view ,name='signup'),
    path('list/',views.list_view ,name='list'),
]
