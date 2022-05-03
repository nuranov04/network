from rest_framework.routers import DefaultRouter

from apps.post.views import PostViewSet, PostImageViewSet, LikeViewSet

router = DefaultRouter()
router.register(
    prefix='post',
    viewset=PostViewSet
)
router.register(
    prefix='post_image',
    viewset=PostImageViewSet
)
router.register(
    prefix='like',
    viewset=LikeViewSet
)

urlpatterns = router.urls
