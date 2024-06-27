from django.urls import path
from .views import post_detail, post_list

app_name = 'main'

urlpatterns = [
  path('', post_list, name='post_list'),
  path('<slug:post>/', post_detail, name='post_detail')
]
