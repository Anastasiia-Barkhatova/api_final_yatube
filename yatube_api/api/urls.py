from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_yatube_v1 = DefaultRouter()
router_yatube_v1.register('posts', PostViewSet, basename='posts')
router_yatube_v1.register('groups', GroupViewSet, basename='groups')
router_yatube_v1.register('follow', FollowViewSet, basename='follow')
router_yatube_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)

api_urls = [
    path('', include(router_yatube_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(api_urls))
]
