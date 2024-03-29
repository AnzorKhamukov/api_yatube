from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet


router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
