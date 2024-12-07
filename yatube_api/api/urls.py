from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('posts', views.PostViewSet,
    basename='posts')
router.register(r'posts/(?<post_id>\d+)/comments',
    views.CommentViewSet, basename='comments')
router.register('groups',
    views.GroupViewSet, basename='groups')
router.register('follow',
    views.FollowViewSet, basename='follow')


url_patterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
