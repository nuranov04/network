from rest_framework.routers import DefaultRouter

from apps.user.views import UserViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=UserViewSet
)

urlpatterns = router.urls