from rest_framework.routers import DefaultRouter

from .views import (
    PromotionViewSet,
    InscriptionViewSet,
    CoursPlanifieViewSet,
    AnimerViewSet
)

router = DefaultRouter()

router.register(r'promotions', PromotionViewSet)
router.register(r'inscriptions', InscriptionViewSet)
router.register(r'cours-planifies', CoursPlanifieViewSet)
router.register(r'animer', AnimerViewSet)

urlpatterns = router.urls