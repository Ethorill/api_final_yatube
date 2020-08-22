from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from .views import PostViewSetApi, CommentViewSetApi, GroupViewSetApi, FlowViewSetApi

router = routers.DefaultRouter()
router.register('posts', PostViewSetApi, basename='posts')
router.register('group', GroupViewSetApi, basename='groups'),
router.register('follow', FlowViewSetApi, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSetApi,
                basename='comments'
                )


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view()),
    path('v1/token/refresh/', TokenRefreshSlidingView.as_view())
]
