from django.urls import path
from .views import post_list, post_detail

app_name = 'shop'
urlpatterns = [
# post views
    path('', post_list, name='shop_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    post_detail,
    name='post_detail'),
 ]