from django.urls import path
 
# importing views from views..py
from .views import create_view, list_view, detail_view, update_view, delete_view
 
urlpatterns = [
    path('create/', create_view),
    path('list/', list_view),
    path('list/<id>', detail_view),
    path('list/<id>/update', update_view),
    path('list/<id>/delete', delete_view),
]