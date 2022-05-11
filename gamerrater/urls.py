from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from gamerraterapi.views import GameView, GameCategoryView, login_user, register_user
from rest_framework import routers

from gamerraterapi.views.category import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'gamecategories', GameCategoryView, 'gamecategory')
router.register(r'categories', CategoryView, 'category')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
