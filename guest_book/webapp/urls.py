from django.urls import path

from webapp.views import index_view, create_view, \
    update_view, delete_view, index_create_view, \
    search_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create/', create_view, name='create_view'),
    path('update/<int:pk>', update_view, name='update_view'),
    path('delete/<int:pk>', delete_view, name='delete_view'),
    path('create/index', index_create_view, name='index_create_view'),
    path('search', search_view, name='search_view')
]
