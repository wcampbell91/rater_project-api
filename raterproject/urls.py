from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from raterapi.views import GamesViewSet, CategoriesViewSet, GameReviewViewSet, register_user, login_user, GameRatingViewSet, PlayerViewSet, GamePictureViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GamesViewSet, 'game')
router.register(r'categories', CategoriesViewSet, 'category')
router.register(r'reviews', GameReviewViewSet, 'review')
router.register(r'ratings', GameRatingViewSet, 'rating')
router.register(r'players', PlayerViewSet, 'player')
router.register(r'pictures', GamePictureViewSet, 'picture')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
