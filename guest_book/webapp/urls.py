from django.urls import path

from webapp.views import index_view, create_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create/', create_view, name='create_view'),

]
