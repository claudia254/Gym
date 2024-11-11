
from django.urls import path

from gymapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('trainer',views.trainer,name='trainer'),
    path('why',views.why,name='why'),

]
