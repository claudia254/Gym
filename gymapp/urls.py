
from django.urls import path

from gymapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('trainer',views.trainer,name='trainer'),
    path('why',views.why,name='why'),

]
