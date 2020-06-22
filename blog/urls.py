from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_sites,name='all_sites'),
    path('<int:blog_id>/',views.detail,name='detail'),


]
