from django.urls import path
from .views import top_5_ratings_list, bottom_5_ratings_list 

urlpatterns = [
    path('reports/top5ratings', top_5_ratings_list),
    path('reports/bottom5ratings', bottom_5_ratings_list)
]
