from django.urls import path
from .views import HOME,UPDATE,CREATE,SEE_PROFILE,DELETE

urlpatterns = [
    path('',HOME,name='home'),
    path('update/<str:id>/',UPDATE,name='update'),
    path('create/',CREATE,name='create'),
    path('seeProfile/<str:id>/',SEE_PROFILE,name='seeProfile'),
    path('delete/<str:id>/',DELETE,name='delete'),
]

