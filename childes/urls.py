from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:transcript_id>/', views.detail, name='detail'),
    path('search/', views.SearchPage, name='search_result'),
    # path('parse-excel/', views.ParseExcel.as_view(), name='parse'),
    # path('upload/', views.parse),
]