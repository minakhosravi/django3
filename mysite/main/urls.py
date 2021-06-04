from django.urls import path
from .views import post_list, post_detail

app_name = 'main'
urlpatterns = [
# post views
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    post_detail,
    name='post_detail'),
]