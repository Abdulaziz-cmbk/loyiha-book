from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),

    #author
    path('author/', views.author_view, name="author_view"),
    path('author/create', views.author_create, name='author_create'),
    path('author/update/<int:pk>', views.author_update, name='author_update'),
    path('author/delete/<int:pk>', views.author_delete, name='author_delete'),

    #refrences
    path('reference/', views.reference_view,name='reference_view'),
    path('reference/create', views.reference_create, name='reference_create'),
    path('reference/update/<int:pk>', views.reference_update, name='reference_update'),
    path('reference/delete/<int:pk>', views.reference_delete, name='reference_delete'),
]
