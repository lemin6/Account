from django.urls import path
from .views import AuthorViewSets

urlpatterns = [
    path('', AuthorViewSets.as_view({'get': 'list', 'post': 'create'}), name='author_list'),
    path('<int:pk>/', AuthorViewSets.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='author_detail'),

]