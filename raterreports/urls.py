from django.urls import path
from .views import top_5_ratings_list, bottom_5_ratings_list, GamesPerCategory, more_than_5

urlpatterns = [
    path('reports/top5ratings', top_5_ratings_list),
    path('reports/bottom5ratings', bottom_5_ratings_list),
    path('reports/gamespercategory', GamesPerCategory),
    path('reports/morethan5players', more_than_5),
]
